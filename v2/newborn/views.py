from django.core import serializers
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from newborn.models import Newborn, NewbornAdmission, MotherDetails, MotherLocation, LabRequest, LabResult, Patient, NewbornExam,Subcounty, Parish, Village, CountyMunicipality
from newborn.forms import NewbornForm, LabTestRequestForm, LabResultForm, MothersAntenatalDetailsForm, NewbornAdmissionForm, MotherDetailForm, MotherLocationForm, PatientForm, NewbornExamForm, AntenatalHistoryForm
from .tables import NewbornTable
from .filters import NewbornFilter
from newborn.serializers import NewbornSerializer
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Q
from datetime import date, timedelta, datetime
import json
from django_tables2 import RequestConfig

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
def antenatal_hx(request):
    if request.method == 'POST':
        form = AntenatalHistoryForm(request.POST)        
        if form.is_valid():
            instance = form.save()
            instance.mother = MotherDetails.objects.all().order_by('-id')[0]
            instance.save()
            return redirect('home-page')
    else:
        form = AntenatalHistoryForm()
    return render(request, 'newborn/antenatal_details.html', {'form': form})


@login_required
def lab_request(request, pk):
    neonate = get_object_or_404(NewbornAdmission, pk=pk)

    if request.method == 'POST':
        form = LabTestRequestForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.neonate = neonate
            instance.author = request.user
            instance.timestamp = timezone.now()

            # Set the specific test fields to True based on user selection
            instance.serology_rpr_requested = form.cleaned_data['serology_rpr_requested']
            instance.serology_rct_requested = form.cleaned_data['serology_rct_requested']
            instance.serology_bat_requested = form.cleaned_data['serology_bat_requested']
            instance.microbiology_gram_stain_requested = form.cleaned_data['microbiology_gram_stain_requested']
            instance.microbiology_culture_requested = form.cleaned_data['microbiology_culture_requested']
            instance.chemistry_serum_electrolytes_requested = form.cleaned_data['chemistry_serum_electrolytes_requested']
            instance.chemistry_serum_urea_requested = form.cleaned_data['chemistry_serum_urea_requested']
            instance.chemistry_serum_creatinine_requested = form.cleaned_data['chemistry_serum_creatinine_requested']
            instance.chemistry_urinalysis_requested = form.cleaned_data['chemistry_urinalysis_requested']

            instance.save()
            return redirect(reverse('clerkship-page', kwargs={'pk': pk}))
    else:
        form = LabTestRequestForm()

    return render(request, 'newborn/lab_request2.html', {'form': form})


def home(request):
    return render(request, 'newborn/home.html', {'title': 'Home'})

def newborn_table(request):
    table = NewbornTable(NewbornAdmission.objects.all().order_by('-id')[:4])

    return render(request, 'newborn/home.html', {'table': table})

@login_required
def newborn_search(request):
    searched = request.GET.get('searched', '')
    newborns = None

    if searched.isdigit():
        newborns = NewbornTable(NewbornAdmission.objects.filter(Q(pk=int(searched))))
    else:
        newborns = NewbornTable(NewbornAdmission.objects.filter(Q(name__contains=searched)))

    RequestConfig(request).configure(newborns)

    return render(request, 'newborn/search.html', {'searched': searched, 'newborns': newborns})
########
#more

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

    # Retrieve LabRequests for pending tests
    pending_lab_requests = LabRequest.objects.filter(neonate=newborn, labresult__isnull=True)

    context = {
        'newborn': newborn,
        'age_days': age_days,
        'age_hours': age_hours,
        'age_minutes': age_minutes,
        'lab_results': lab_results,
        'pending_lab_requests': pending_lab_requests,
    }
    return render(request, 'newborn/patient2.html', context)


def print_clerkship(request):
    context = {
          'newborn': NewbornAdmission.objects.all().order_by('-id')[0]
    }
    return render(request, 'newborn/clerkship.html', context)


def dashboard(request):
    # Retrieve data for charts
    sex_data = NewbornAdmission.objects.values('sex')\
                             .annotate(num_sex=Count('id'))

    diagnosis_data = NewbornAdmission.objects.values('diagnosis')\
                                    .annotate(num_dx=Count('id'))

    # Retrieve data for lists
    new_admissions = NewbornAdmission.objects.filter(admission_date=date.today())

    # Render template with data
    return render(request, 'newborn/dashboard3.html', {
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
        print(form)
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


def lab_requests_dashboard(request):
    # Retrieve neonates with pending lab results
    neonates_with_pending_results = []
    lab_requests = LabRequest.objects.all()

    for lab_request in lab_requests:
        # Get the neonate associated with the lab request
        neonate = lab_request.neonate
        # Set the labrequest attribute
        neonate.labrequest = lab_request

        # Calculate age in days
        age_delta = neonate.admission_date.date() - neonate.delivery_date.date()
        age_days = age_delta.days

        # Calculate time elapsed as timedelta
        time_elapsed = timezone.now() - lab_request.timestamp

        # Convert time_elapsed to a datetime object
        time_elapsed_datetime = timezone.now() - time_elapsed

        # Count the number of tests requested for this lab request
        num_tests_requested = sum([
            lab_request.serology_rpr_requested,
            lab_request.serology_rct_requested,
            lab_request.serology_bat_requested,
            lab_request.microbiology_gram_stain_requested,
            lab_request.microbiology_culture_requested,
            lab_request.chemistry_serum_electrolytes_requested,
            lab_request.chemistry_serum_urea_requested,
            lab_request.chemistry_serum_creatinine_requested,
            lab_request.chemistry_urinalysis_requested,
        ])

        # Check if any lab test was requested for this lab request
        if num_tests_requested > 0:
            neonate.age_days = age_days
            neonate.time_elapsed = time_elapsed_datetime
            neonate.num_tests_requested = num_tests_requested
            neonates_with_pending_results.append(neonate)

    context = {
        'neonates_with_pending_results': neonates_with_pending_results,
    }
    return render(request, 'newborn/lab_requests_dashboard.html', context)


def input_lab_results(request, neonate_pk, lab_request_pk):
    neonate = get_object_or_404(NewbornAdmission, pk=neonate_pk)
    lab_request = get_object_or_404(LabRequest, pk=lab_request_pk, neonate=neonate)

    if request.method == 'POST':
        form = LabResultForm(request.POST, lab_request=lab_request)
        if form.is_valid():
            lab_result = form.save(commit=False)
            lab_result.lab_request = lab_request
            lab_result.neonate = neonate  # Set the neonate
            lab_result.author = request.user  # Set the author

            lab_result.save()

            # Mark the specific test fields as completed
            if lab_result.serology_rpr_result:
                lab_request.serology_rpr_requested = False
            if lab_result.serology_rct_result:
                lab_request.serology_rct_requested = False
            if lab_result.serology_bat_result:
                lab_request.serology_bat_requested = False
            if lab_result.microbiology_gram_stain_result:
                lab_request.microbiology_gram_stain_requested = False
            if lab_result.microbiology_culture_result:
                lab_request.microbiology_culture_requested = False
            if lab_result.chemistry_serum_electrolytes_result:
                lab_request.chemistry_serum_electrolytes_requested = False
            if lab_result.chemistry_serum_urea_result:
                lab_request.chemistry_serum_urea_requested = False
            if lab_result.chemistry_serum_creatinine_result:
                lab_request.chemistry_serum_creatinine_requested = False
            if lab_result.chemistry_urinalysis_result:
                lab_request.chemistry_urinalysis_requested = False

            lab_request.save()

            # Generate the URL for the lab requests dashboard view
            dashboard_url = reverse('lab-requests-dashboard')

            # Redirect back to the dashboard
            return redirect(dashboard_url)
    else:
        form = LabResultForm(lab_request=lab_request)

    return render(request, 'newborn/input_lab_results.html', {
        'neonate': neonate,
        'lab_request': lab_request,
        'lab_request_pk': lab_request_pk,
        'form': form,
    })
