from django.core import serializers
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser
from newborn.models import NewbornAdmission, MothersAntenatalDetails, MotherDetails, MotherLocation, NewbornExam,Subcounty, Parish, Village, CountyMunicipality
from newborn.forms import MothersAntenatalDetailsForm, NewbornAdmissionForm, MotherDetailForm, MotherLocationForm, NewbornExamForm
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Avg, Count, Q
from datetime import date, timedelta, datetime
import json
from django_tables2 import RequestConfig
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.timesince import timesince
from functools import wraps
from django.contrib import messages
from lab.models import LabRequest, LabResult
from django.views.decorators.cache import never_cache


@login_required
def index(request):
    latest_mother = MotherDetails.objects.all().order_by('-id').first()
    
    if request.method == 'POST':
        form = NewbornForm(request.POST, initial={'mother': latest_mother})
        if form.is_valid():
            instance = form.save(commit=False)
            instance.mother = latest_mother
            instance.save()
            return redirect('home-page')
    else:
        form = NewbornForm(initial={'mother': latest_mother})
    return render(request, 'newborn/delivery.html', {'form': form})


@login_required
def newborn_search(request):
    searched = request.GET.get('searched_item', '')
    newborns = None

    if searched.isdigit():
        newborns = NewbornAdmission.objects.filter(pk=int(searched))
    else:
        newborns = NewbornAdmission.objects.filter(name__contains=searched)
    print('Searched:', searched)
    print("Newborn object", newborns)

    return render(request, 'newborn/search.html', {'searched': searched, 'newborns': newborns})


@login_required
def mother(request):
    if request.method == 'POST':
        location_form = MotherLocationForm(request.POST)
        detail_form = MotherDetailForm(request.POST)
        
        if location_form.is_valid() and detail_form.is_valid():
            location_instance = location_form.save(commit=False)
            location_instance.save()

            detail_instance = detail_form.save(commit=False)
            detail_instance.location = location_instance
            detail_instance.save()
            
            # Rest of your code to save the instances and redirect
            return redirect('newborn-delivery')
            
    else:
        detail_form = MotherDetailForm()
        location_form = MotherLocationForm(is_update=False)

    context = {
        'detail_form': detail_form,
        'location_form': location_form,
    }

    return render(request, 'newborn/mother3.html', context)


def print_detail(request, pk):
    newborn = NewbornAdmission.objects.get(pk=pk)
    age_delta = newborn.admission_date.date() - newborn.delivery_date.date()
    age_days = age_delta.days
    context = {
            'newborn': newborn,
            'age_days': age_days,
    }

    return render(request, 'newborn/details.html', context)


def print_care2x(request, pk):
    newborn = get_object_or_404(NewbornAdmission, pk=pk)  # Retrieve the Newborn object

    # Calculate age_delta as before
    if newborn.referral_date_time:
        age_delta = newborn.admission_date - newborn.referral_date_time
    else:
        age_delta = timedelta(days=0, seconds=0)

    age_days = age_delta.days
    age_hours, remainder_seconds = divmod(age_delta.seconds, 3600)
    age_minutes, _ = divmod(remainder_seconds, 60)

    # Retrieve LabResults associated with this neonate
    lab_results = LabResult.objects.filter(neonate=newborn)

    # Filter LabRequests for pending tests
    pending_lab_requests = LabRequest.objects.filter(
        neonate=newborn
    ).exclude(
        Q(serology_rpr_requested=True, labresult__serology_rpr_result__isnull=False) |
        Q(serology_rct_requested=True, labresult__serology_rct_result__isnull=False) |
        Q(serology_bat_requested=True, labresult__serology_bat_result__isnull=False) |
        Q(microbiology_gram_stain_requested=True, labresult__microbiology_gram_stain_result__isnull=False) |
        Q(microbiology_culture_requested=True, labresult__microbiology_culture_result__isnull=False) |
        Q(chemistry_serum_electrolytes_requested=True, labresult__chemistry_serum_electrolytes_result__isnull=False) |
        Q(chemistry_serum_urea_requested=True, labresult__chemistry_serum_urea_result__isnull=False) |
        Q(chemistry_serum_creatinine_requested=True, labresult__chemistry_serum_creatinine_result__isnull=False) |
        Q(chemistry_urinalysis_requested=True, labresult__chemistry_urinalysis_result__isnull=False)
        # Add conditions for other test fields similarly
    )

    # Retrieve Mother's Antenatal History
    mother = newborn.mother  # Get the associated mother
    antenatal_history = MothersAntenatalDetails.objects.filter(mother=mother).first()

    # Retrieve Newborn Examination Details
    newborn_exams = NewbornExam.objects.filter(neonate=newborn).first()

    context = {
        'newborn': newborn,
        'age_days': age_days,
        'age_hours': age_hours,
        'age_minutes': age_minutes,
        'lab_results': lab_results,
        'pending_lab_requests': pending_lab_requests,
        'antenatal_history': antenatal_history,
        'newborn_exams': newborn_exams,
    }
    return render(request, 'newborn/patient2.html', context)

def print_clerkship(request):
    context = {
          'newborn': NewbornAdmission.objects.all().order_by('-id')[0]
    }
    return render(request, 'newborn/clerkship.html', context)


def discharge_form(request, pk):
    newborn = NewbornAdmission.objects.get(pk=pk)
    return render(request, 'newborn/discharge_form.html', {'newborn': newborn})


def newborn_exam_form(request, pk):
    neonate = get_object_or_404(NewbornAdmission, pk=pk)
    try:
        exam = NewbornExam.objects.get(neonate=neonate)
    except NewbornExam.DoesNotExist:
        exam = None

    if request.method == 'POST':
        form = NewbornExamForm(request.POST, instance=exam)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.neonate = neonate
            instance.save()
            return redirect(reverse('clerkship-page', kwargs={'pk': pk}))
    else:
        form = NewbornExamForm(instance=exam)

    return render(request, 'newborn/newborn_exam_form.html', {'form': form})


def update_details(request, pk):
    newborn = get_object_or_404(NewbornAdmission, pk=pk)
    mother = newborn.mother
    location = mother.location
    antenatal_history = mother.mothersantenataldetails_set.first()

    if request.method == 'POST':
        location_form = MotherLocationForm(request.POST, prefix='location', instance=location, is_update=True)
        detail_form = MotherDetailForm(request.POST, prefix='detail', instance=mother)
        antenatal_form = MothersAntenatalDetailsForm(request.POST, prefix='antenatal', instance=antenatal_history)
        #print(location_form)

        if (
            location_form.is_valid()
            and detail_form.is_valid()
            and antenatal_form.is_valid()
        ):
            location_instance = location_form.save()
            detail_instance = detail_form.save(commit=False)
            detail_instance.location = location_instance
            detail_instance.save()
            antenatal_instance = antenatal_form.save(commit=False)
            antenatal_instance.mother = detail_instance
            antenatal_instance.save()

            return redirect(reverse('clerkship-page', kwargs={'pk': pk}))
    else:
        location_form = MotherLocationForm(prefix='location', instance=location, is_update=True)
        detail_form = MotherDetailForm(prefix='detail', instance=mother)
        antenatal_form = MothersAntenatalDetailsForm(prefix='antenatal', instance=antenatal_history)

    return render(request, 'newborn/update_details.html', {
        'location_form': location_form,
        'detail_form': detail_form,
        'antenatal_form': antenatal_form,
    })


def fetch_county_municipalities(request, district_id):
    county_municipalities = CountyMunicipality.objects.filter(district_id=district_id).values('id', 'name')
    data = {'county_municipalities': list(county_municipalities)}
    return JsonResponse(data)

def fetch_subcounties(request, county_municipality_id):
    subcounties = Subcounty.objects.filter(county_municipality_id=county_municipality_id).values('id', 'name')
    data = {'subcounties': list(subcounties)}
    return JsonResponse(data)

def fetch_parishes(request, subcounty_id):
    parishes = Parish.objects.filter(subcounty_id=subcounty_id).values('id', 'name')
    data = {'parishes': list(parishes)}
    return JsonResponse(data)

def fetch_villages(request, parish_id):
    villages = Village.objects.filter(parish_id=parish_id).values('id', 'name')
    data = {'villages': list(villages)}
    return JsonResponse(data)


def mothers_antenatal_details(request, pk):
    # Get the newborn object using the provided primary key (pk)
    newborn = get_object_or_404(NewbornAdmission, pk=pk)

    if request.method == 'POST':
        form = MothersAntenatalDetailsForm(request.POST)
        #print(form.error)
        if form.is_valid():
            # Save the form data to the mother's antenatal details
            antenatal_details = form.save(commit=False)  # Create an object from the form data, but don't save it yet
            antenatal_details.mother = newborn.mother  # Associate the mother object with the newborn's mother
            antenatal_details.save()  # Now save the antenatal details with the associated mother

            return redirect(reverse('clerkship-page', kwargs={'pk': pk}))
    else:
        form = MothersAntenatalDetailsForm()

    return render(request, 'newborn/newborn_admission_form.html', {'form': form})


def newborn_admission(request):
    latest_mother = MotherDetails.objects.all().order_by('-id').first()

    if request.method == 'POST':
        form = NewbornAdmissionForm(request.POST, initial={'mother': latest_mother})
        print(form.errors)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.mother = latest_mother
            instance.save()
            
            return redirect('home-page')  # Redirect to a success page
    else:
        form = NewbornAdmissionForm(initial={'mother': latest_mother})
    return render(request, 'newborn/newborn_delivery_notes.html', {'form': form})


@never_cache
@login_required
def landing_page(request):
    table = NewbornAdmission.objects.all().order_by('-id')[:4]

    return render(request, 'newborn/landing_page.html', {'table': table})
