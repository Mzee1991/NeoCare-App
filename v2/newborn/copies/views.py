from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from newborn.models import Newborn
from newborn.forms import NewbornForm
from newborn.serializers import NewbornSerializer
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.views import generic

class CreateView(generic.edit.CreateView):
    model = Newborn
    fields = ["name", "admission_date", "gestation_age", "diagnosis", "discharge_date"]
    def get_form(self):
        form = super().get_form()
        
        form.fields["admission_date"].widget = DatePickerInput(
            attrs={"class": "my-exclusive-input"},
            options={
                "format": "DD-MM-YYYY",
                "showTodayButton": False,
            },
        )
        
        form.fields["discharge_date"].widget = DatePickerInput(
            attrs={"class": "my-exclusive-input"},
            options={
                "format": "DD-MM-YYYY",
                "showTodayButton": False,
            },
        )
        return form

def newborn_list(request):
    """
    list all newborns, or enter newborn into the system.
    """
    if request.method == 'GET':
        newborns = Newborn.objects.all()
        serializer = NewbornSerializer(newborns, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NewbornSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def newborn_detail(request, pk):
    """
    Retrieve, update or delete a newborn
    """
    try:
        newborn = Newborn.objects.get(pk=pk)
    except Newborn.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NewbornSerializer(newborn)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NewbornSerializer(newborn, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        newborn.delete()
        return HttpResponse(status=204)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def index(request):
    form = NewbornForm()
    
    if request.method == 'POST':
        form = NewbornForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'newborn/index.html')
