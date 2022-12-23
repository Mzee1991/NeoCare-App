from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from newborn.models import Newborn, MotherDetails, MotherLocation
from newborn.forms import NewbornForm, MotherDetailForm, MotherLocationForm
from .tables import NewbornTable
from .filters import NewbornFilter
from newborn.serializers import NewbornSerializer
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

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

@login_required
def index(request):
    if request.method == 'POST':
        form = NewbornForm(request.POST)        
        if form.is_valid():
            instance = form.save()
            instance.mother = MotherDetails.objects.all().order_by('-id')[0]
            instance.save()
            return redirect('home-page')
    else:
        form = NewbornForm()
    return render(request, 'newborn/index.html', {'form': form})

def home(request):
    return render(request, 'newborn/home.html', {'title': 'Home'})

def newborn_table(request):
    table = NewbornTable(Newborn.objects.all().order_by('-id')[:4])

    return render(request, 'newborn/home.html', {'table': table})

@login_required
def newborn_search(request):
    if request.method == 'GET':
        searched = request.GET.get('searched', False)
        newborns = NewbornTable(Newborn.objects.filter(name__contains=searched))
        return render(request, 'newborn/search.html', {'searched': searched, 'newborns': newborns})
    else:
        return render(request, 'newborn/search.html', {})

########
#more

@login_required
def mother(request):
    if request.method == 'POST':
        location_form = MotherLocationForm(request.POST)
        if location_form.is_valid():
            location_form.save()
            detail_form = MotherDetailForm(request.POST)
            if detail_form.is_valid():
                instance = detail_form.save()
                instance.location = MotherLocation.objects.all().order_by('-id')[0]
                instance.save()
                return redirect('add-newborn')
    else:
        detail_form = MotherDetailForm()
        location_form = MotherLocationForm()
        context = {'detail_form': detail_form, 'location_form': location_form}
    return render(request, 'newborn/mother.html/', context)

def print_detail(request):
    context = {
        'newborn': Newborn.objects.all().order_by('-id')[0]
    }
    return render(request, 'newborn/patient.html', context)
