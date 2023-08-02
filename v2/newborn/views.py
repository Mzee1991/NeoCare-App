from django.core import serializers
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from newborn.models import Newborn, NewbornAdmission, MotherDetails, MotherLocation, LabInvestigation, Patient, NewbornExam, LabInvestigation, Subcounty, Parish, Village, CountyMunicipality
from newborn.forms import NewbornForm, LabTestRequestForm, LabTestResultForm, MothersAntenatalDetailsForm, NewbornAdmissionForm, MotherDetailForm, MotherLocationForm, PatientForm, NewbornExamForm, AntenatalHistoryForm
from .tables import NewbornTable
from .filters import NewbornFilter
from newborn.serializers import NewbornSerializer
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Q
from datetime import date, timedelta
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
    try:
        lab_investigation = LabInvestigation.objects.get(neonate=neonate)
    except LabInvestigation.DoesNotExist:
        lab_investigation = None

    if request.method == 'POST':
        form = LabTestRequestForm(request.POST, instance=lab_investigation)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.neonate = neonate

            # Set the author as the currently logged-in user (assuming you have implemented authentication)
            instance.author = request.user

            # Set the timestamp to the current date and time
            instance.timestamp = timezone.now()

            instance.save()
            return redirect(reverse('clerkship-page', kwargs={'pk': pk}))
    else:
        form = LabTestRequestForm(instance=lab_investigation)

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
    newborn = NewbornAdmission.objects.get(pk=pk)  # Retrieve the Newborn object

    # Check if the referral_date_time is not None
    if newborn.referral_date_time:
        age_delta = newborn.admission_date - newborn.referral_date_time
    else:
        # Set age_delta to a default value if referral_date_time is None
        age_delta = timedelta(days=0, seconds=0)

    age_days = age_delta.days
    age_hours, remainder_seconds = divmod(age_delta.seconds, 3600)
    age_minutes, _ = divmod(remainder_seconds, 60)

    mother = newborn.mother  # Access the Mother object associated with the newborn
    antenatal_history = mother.mothersantenataldetails_set.first()  # The Antenatalhistory related to the mother
    # Retrieve the NewbornExam objects related to the newborn
    newborn_exams = newborn.newbornexam_set.first()
    # Retrieve the LabInvestigation objects related to the newborn
    lab_investigation = newborn.labinvestigation_set.first()
    context = {
         'newborn': newborn,
         'mother': mother,
         'antenatal_history': antenatal_history,
         'newborn_exams': newborn_exams,  # Include newborn_exams in the context
         'lab_investigation': lab_investigation,
         'age_days': age_days,
         'age_hours': age_hours,
         'age_minutes': age_minutes,
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
    newborn = Newborn.objects.get(pk=pk)
    return render(request, 'newborn/discharge_form.html', {'newborn': newborn})


#def delivery_view(request):
 #   if request.method == 'POST':
  #      form = DeliveryForm(request.POST)
   #     if form.is_valid():
    #        delivery = form.save()
     #       delivery.save()
      #      return redirect('home-page')
       
    #else:
     #   form = DeliveryForm()
    #return render(request, 'newborn/delivery.html', {'form': form})

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
    lab_requests = LabInvestigation.objects.all()

    if request.method == 'POST':
        form = LabTestResultForm(request.POST)
        if form.is_valid():
            lab_investigation = form.save(commit=False)
            lab_investigation.author = request.user
            lab_investigation.save()
            return redirect('lab-requests-dashboard')  # Redirect to the same page to avoid form resubmission

    else:
        form = LabTestResultForm()

    # Remove patients whose lab tests are complete from the dashboard
    complete_lab_requests = [lab_request for lab_request in lab_requests if lab_request.is_complete()]
    lab_requests = [lab_request for lab_request in lab_requests if not lab_request.is_complete()]

    return render(request, 'newborn/lab_requests_dashboard.html', {'lab_requests': lab_requests, 'complete_lab_requests': complete_lab_requests, 'form': form})

def lab_request_details(request, patient_pk):
    lab_request = get_object_or_404(LabInvestigation, neonate__pk=patient_pk)
    lab_tests = []

    if request.method == 'POST':
        # Check if the 'test_request' parameter is present in the request
        if 'test_request' in request.POST:
            result_form = LabTestRequestForm(request.POST, instance=lab_request)
        else:
            result_form = LabTestResultForm(request.POST, instance=lab_request)

        if result_form.is_valid():
            result_form.save()
            return redirect('lab_request_details', patient_pk=patient_pk)
    else:
        requested_test = request.GET.get('test', None)
        if requested_test:
            lab_tests = [requested_test]
            if requested_test in LabTestRequestForm.Meta.fields:
                # Show lab test request form for the specific test
                result_form = LabTestRequestForm(instance=lab_request, prefix='test_request')
            elif requested_test in LabTestResultForm.Meta.fields:
                # Show lab test result form for the specific test
                result_form = LabTestResultForm(instance=lab_request, prefix=requested_test)
            else:
                result_form = None
        else:
            # No test requested in the URL, display all pending tests
            lab_tests = [field for field in LabTestRequestForm.Meta.fields if getattr(lab_request, field)]
            result_form = None

    return render(request, 'newborn/lab_request_details.html', {
        'lab_request': lab_request,
        'result_form': result_form,
        'requested_test': requested_test,
        'lab_tests': lab_tests,
    })

def lab_save_result(request, patient_pk):
    if request.method == 'POST' and request.is_ajax():
        lab_request = get_object_or_404(LabInvestigation, neonate__pk=patient_pk)
        form = LabTestResultForm(request.POST, instance=lab_request)
        if form.is_valid():
            form.save()

            # Create a dictionary containing all lab test result fields and their values
            lab_test_results = {
                'serology_rpr_result': lab_request.serology_rpr_result,
                'serology_rct_result': lab_request.serology_rct_result,
                'serology_bat_result': lab_request.serology_bat_result,
                'microbiology_gram_stain_result': lab_request.microbiology_gram_stain_result,
                'microbiology_culture_result': lab_request.microbiology_culture_result,
                'chemistry_serum_electrolytes_result': lab_request.chemistry_serum_electrolytes_result,
                'chemistry_serum_urea_result': lab_request.chemistry_serum_urea_result,
                'chemistry_serum_creatinine_result': lab_request.chemistry_serum_creatinine_result,
                'chemistry_urinalysis_result': lab_request.chemistry_urinalysis_result,
            }

            return JsonResponse({'success': True, 'results': lab_test_results})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'error': 'Invalid request'})
