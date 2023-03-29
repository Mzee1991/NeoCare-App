from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from newborn.models import Newborn, MotherDetails, MotherLocation, LabInvestigation, Patient
from newborn.forms import NewbornForm, MotherDetailForm, MotherLocationForm, LabInvestigationForm, BirthRecordForm, PatientForm
from .tables import NewbornTable
from .filters import NewbornFilter
from newborn.serializers import NewbornSerializer
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from datetime import date
import json

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

def lab_request(request):
    if request.method == 'POST':
        form = LabInvestigationForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.save()
            return redirect('home-page')
    else:
        form = LabInvestigationForm()
    return render(request, 'newborn/lab_request.html', {'form': form})

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
    return render(request, 'newborn/mother3.html/', context)

def print_detail(request, pk):
    context = {
            'newborn': Newborn.objects.get(pk=pk)
    }

    return render(request, 'newborn/details.html', context)

def print_care2x(request, pk):
    context = {
         'newborn': Newborn.objects.get(pk=pk)
    }
    return render(request, 'newborn/patient2.html', context)

def print_clerkship(request):
    context = {
          'newborn': Newborn.objects.all().order_by('-id')[0]
    }
    return render(request, 'newborn/clerkship.html', context)


def dashboard(request):
    # Retrieve data for charts
    age_data = Newborn.objects.filter(age_in_days__lte=5)\
                             .values('age_in_days')\
                             .annotate(num_age=Count('id'))

    sex_data = Newborn.objects.values('sex')\
                             .annotate(num_sex=Count('id'))

    diagnosis_data = Newborn.objects.values('diagnosis')\
                                    .annotate(num_dx=Count('id'))

    # Retrieve data for lists
    new_admissions = Newborn.objects.filter(admission_date=date.today())

    # Render template with data
    return render(request, 'newborn/dashboard3.html', {
        'age_data_json': json.dumps(list(age_data)),
        'sex_data_json': json.dumps(list(sex_data)),
        'diagnosis_data_json': json.dumps(list(diagnosis_data)),
        'new_admissions': new_admissions,
    })


def create_birth_record(request):
    if request.method == 'POST':
        form = BirthRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('birth_records')
    else:
        form = BirthRecordForm()
    return render(request, 'newborn/create_birth_record6.html', {'form': form})

def discharge_form(request, pk):
    newborn = Newborn.objects.get(pk=pk)
    return render(request, 'newborn/discharge_form.html', {'newborn': newborn})
