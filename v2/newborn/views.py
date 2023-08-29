from django.core import serializers
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser
from newborn.models import Newborn, NewbornAdmission, Dose1Dispensation, Dose2Dispensation, Dose3Dispensation, Dose4Dispensation, Prescription, MothersAntenatalDetails, MotherDetails, MotherLocation, LabRequest, LabResult, Patient, NewbornExam,Subcounty, Parish, Village, CountyMunicipality
from newborn.forms import NewbornForm, PrescriptionForm, DynamicLabResultForm, LabTestRequestForm, LabResultForm, MothersAntenatalDetailsForm, NewbornAdmissionForm, MotherDetailForm, MotherLocationForm, PatientForm, NewbornExamForm, AntenatalHistoryForm
from .tables import NewbornTable
from .filters import NewbornFilter
from newborn.serializers import NewbornSerializer
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Q
from datetime import date, timedelta, datetime
import json
from django_tables2 import RequestConfig
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.timesince import timesince

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
    searched = request.GET.get('searched_item', '')
    newborns = None

    if searched.isdigit():
        newborns = NewbornAdmission.objects.filter(pk=int(searched))
    else:
        newborns = NewbornAdmission.objects.filter(name__contains=searched)
    print('Searched:', searched)
    print("Newborn object", newborns)

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


@login_required
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
        time_elapsed = (timezone.now() - lab_request.timestamp).total_seconds()

        # Convert time_elapsed to a datetime object
        #time_elapsed_datetime = timezone.now() - time_elapsed

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
            neonate.time_elapsed = time_elapsed
            neonate.num_tests_requested = num_tests_requested
            neonates_with_pending_results.append(neonate)

    context = {
        'neonates_with_pending_results': neonates_with_pending_results,
    }
    return render(request, 'newborn/lab_requests_dashboard.html', context)

def input_lab_result(request, neonate_pk, lab_request_pk, test_name):
    neonate = get_object_or_404(NewbornAdmission, pk=neonate_pk)
    lab_request = get_object_or_404(LabRequest, pk=lab_request_pk, neonate=neonate)

    # Check if the selected test_name is valid
    valid_tests = [
        'serology_rpr', 'serology_rct', 'serology_bat',
        'microbiology_gram_stain', 'microbiology_culture',
        'chemistry_serum_electrolytes', 'chemistry_serum_urea',
        'chemistry_serum_creatinine', 'chemistry_urinalysis'
    ]

    if test_name not in valid_tests:
        return HttpResponse("Invalid test name")

    lab_result = None  # Initialize lab_result, it will be used in case of form submission

    if request.method == 'POST':
        form = DynamicLabResultForm(request.POST, test_name=test_name, instance=lab_result)
        if form.is_valid():
            lab_result = form.save(commit=False)
            lab_result.lab_request = lab_request
            lab_result.neonate = neonate
            lab_result.author = request.user
            lab_result.save()

            setattr(lab_request, f'{test_name}_requested', False)
            lab_request.save()

            return redirect('pending-lab-tests', neonate_pk=neonate_pk, lab_request_pk=lab_request_pk)
    else:
        form = DynamicLabResultForm(test_name=test_name, instance=lab_result)

    context = {
        'neonate': neonate,
        'lab_request': lab_request,
        'form': form,
        'lab_request_pk': lab_request_pk,
        'test_name': test_name,
    }
    return render(request, 'newborn/input_lab_results.html', context)


def pending_lab_tests(request, neonate_pk, lab_request_pk):
    neonate = get_object_or_404(NewbornAdmission, pk=neonate_pk)
    lab_request = get_object_or_404(LabRequest, pk=lab_request_pk, neonate=neonate)

    if not any([
        lab_request.serology_rpr_requested,
        lab_request.serology_rct_requested,
        lab_request.serology_bat_requested,
        lab_request.microbiology_gram_stain_requested,
        lab_request.microbiology_culture_requested,
        lab_request.chemistry_serum_electrolytes_requested,
        lab_request.chemistry_serum_urea_requested,
        lab_request.chemistry_serum_creatinine_requested,
        lab_request.chemistry_urinalysis_requested,
        # Add other test types as needed
    ]):
        return redirect(reverse('lab-requests-dashboard'))

    context = {
        'neonate': neonate,
        'lab_request': lab_request,
    }
    return render(request, 'newborn/pending_lab_tests.html', context)


@login_required
def landing_page(request):
    table = NewbornAdmission.objects.all().order_by('-id')[:4]

    return render(request, 'newborn/landing_page.html', {'table': table})


def calculate_frequency_count(frequency):
    if frequency == 'Once Daily':
        return 1
    elif frequency == 'Twice Daily':
        return 2
    elif frequency == 'Three Times Daily':
        return 3
    elif frequency == 'Four Times Daily':
        return 4
    return 0

@login_required
def patient_treatment_chart(request, admission_id):
    admission = NewbornAdmission.objects.get(id=admission_id)
    admission_date = admission.admission_date
    delivery_date = admission.delivery_date
    
    current_datetime = timezone.now()
    age_delta = current_datetime - delivery_date
    hospital_stay = current_datetime - admission_date
    hospital_duration = timesince(admission_date, current_datetime)

    hospital_days = hospital_stay.days
    hospital_hours, remainder_seconds = divmod(hospital_stay.seconds, 3600)
    hospital_minutes, _ = divmod(remainder_seconds, 60)

    age_days = age_delta.days

    day_dates = []  # Initialize day_dates as an empty list

    if request.method == 'POST':
        form = PrescriptionForm(request.POST, user=request.user)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.admission = admission
            prescription.save()
            return redirect('patient_treatment_chart', admission_id=admission_id)
    else:
        form = PrescriptionForm(user=request.user)

    prescriptions = Prescription.objects.filter(admission=admission)

    if prescriptions:
        start_date = prescriptions[0].start_date
        num_days = 4
        # Create a list of dates for the specified number of days
        day_dates = [start_date + timedelta(days=i) for i in range(num_days)]
    else:
        num_days = 0  # No prescriptions, so no days to display
    
    # Calculate and set frequency count for each prescription
    for prescription in prescriptions:
        prescription.frequency_count = calculate_frequency_count(prescription.frequency)

    context = {
        'num_days': num_days,
        'day_dates': day_dates,
        'prescriptions': prescriptions,
        'admission': admission,
        'form': form,
        'age_days': age_days,
        'hospital_days': hospital_days,
        'hospital_hours': hospital_hours,
        'hospital_minutes': hospital_minutes,
        'hospital_duration': hospital_duration,
    }

    return render(request, 'newborn/prescription.html', context)


def calculate_dosing_times(frequency, start_time):
    dosing_times = [start_time]  # Initialize with the start time

    if frequency == 'Twice Daily':
        dosing_times.append((timezone.datetime.strptime(start_time, '%H:%M') + timezone.timedelta(hours=12)).strftime('%H:%M'))
    elif frequency == 'Three Times Daily':
        dosing_times.extend([
            (timezone.datetime.strptime(start_time, '%H:%M') + timezone.timedelta(hours=8)).strftime('%H:%M'),
            (timezone.datetime.strptime(start_time, '%H:%M') + timezone.timedelta(hours=16)).strftime('%H:%M')
        ])
    elif frequency == 'Four Times Daily':
        dosing_times.extend([
            (timezone.datetime.strptime(start_time, '%H:%M') + timezone.timedelta(hours=6)).strftime('%H:%M'),
            (timezone.datetime.strptime(start_time, '%H:%M') + timezone.timedelta(hours=12)).strftime('%H:%M'),
            (timezone.datetime.strptime(start_time, '%H:%M') + timezone.timedelta(hours=18)).strftime('%H:%M')
        ])

    return dosing_times

@login_required
def save_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, user=request.user)
        admission_id = request.POST.get('admission_id')
        admission = get_object_or_404(NewbornAdmission, id=int(admission_id))
        
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.admission = admission
            prescription.treatment_status = 'Pending'
            prescription.dispenser = None
            prescription.start_date = date.today()

            # Retrieve the prescriber based on the user.id
            prescriber_id = request.POST.get('prescriber')
            try:
                prescriber = User.objects.get(id=prescriber_id)
                prescription.prescriber = prescriber
            except User.DoesNotExist:
                # Handle the case where the user with the provided ID doesn't exist
                pass

            # Calculate dosing times based on frequency and start time
            frequency = request.POST.get('frequency')
            start_time = request.POST.get('start_time')
            dosing_times = calculate_dosing_times(frequency, start_time)

            # Assign dosing times to prescription fields
            prescription.start_dose_time = dosing_times[0]
            prescription.second_dose_time = dosing_times[1] if len(dosing_times) > 1 else None
            prescription.third_dose_time = dosing_times[2] if len(dosing_times) > 2 else None
            prescription.fourth_dose_time = dosing_times[3] if len(dosing_times) > 3 else None

            prescription.save()
            
            # Redirect to the patient_treatment_chart page
            chart_url = reverse('patient_treatment_chart', args=[admission_id])
            return HttpResponseRedirect(chart_url)

        return JsonResponse({'error': form.errors}, status=400)

    return render(request, 'newborn/prescription.html')



def get_dispensation_status(request, dispensation_id):
    try:
        dispensation = Dispensation.objects.get(id=dispensation_id)
        treatment_status = dispensation.treatment_status
        is_locked = dispensation.is_locked

        return JsonResponse({'status': treatment_status, 'is_locked': is_locked})
    except Dispensation.DoesNotExist:
        return JsonResponse({'error': 'Dispensation not found'}, status=404)

def get_prescription_details(request):
    prescription_id = request.GET.get('prescription_id')
    
    try:
        prescription = Prescription.objects.get(id=prescription_id)
        
        # Initialize a list for dose times
        dose_times = []
        
        # Check and add each dose time if it's not None
        if prescription.start_dose_time:
            dose_times.append(prescription.start_dose_time.strftime('%H:%M %p'))
        if prescription.second_dose_time:
            dose_times.append(prescription.second_dose_time.strftime('%H:%M %p'))
        if prescription.third_dose_time:
            dose_times.append(prescription.third_dose_time.strftime('%H:%M %p'))
        if prescription.fourth_dose_time:
            dose_times.append(prescription.fourth_dose_time.strftime('%H:%M %p'))
        
        data = {
            'success': True,
            'prescription': {
                'name': prescription.name,
                'frequency': prescription.frequency,
                'dose_times': dose_times
            }
        }
    except Prescription.DoesNotExist:
        data = {'success': False}
    
    return JsonResponse(data)


def get_dose1_status(request, prescription_id, dispensation_date):
    try:
        prescription = Prescription.objects.get(id=prescription_id)
        # Calculate the number of dose times based on the selected frequency
        num_dose_times = {
            'Once Daily': 1,
            'Twice Daily': 2,
            'Three Times Daily': 3,
            'Four Times Daily': 4,
        }[prescription.frequency]

        # Check if the prescription has at least one dose time (for dose1_status)
        if num_dose_times >= 1:
            # Retrieve the Dose1Dispensation for the given date
            dispensation = Dose1Dispensation.objects.filter(
                prescription_id=prescription_id,
                dispensation_datetime__date=dispensation_date,
            ).last()

            if dispensation:
                dose1_status = getattr(dispensation, 'dose1_status', None)
                dispenser_name = dispensation.dispenser.username if dose1_status == 'Given' else None
            else:
                dose1_status = None
                dispenser_name = None

            # You can customize status_choices based on your model
            status_choices = [
                {'value': choice[0], 'label': choice[1]}
                for choice in Dose1Dispensation.TREATMENT_STATUS_CHOICES
            ]

            return JsonResponse({'dose1_status': dose1_status, 'dispenser_name': dispenser_name, 'status_choices': status_choices})

        else:
            return JsonResponse({'error': 'Prescription does not have at least one dose time.'}, status=400)

    except Prescription.DoesNotExist:
        return JsonResponse({'error': 'Prescription not found.'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_dose2_status(request, prescription_id, dispensation_date):
    try:
        prescription = Prescription.objects.get(id=prescription_id)
        # Calculate the number of dose times based on the selected frequency
        num_dose_times = {
            'Once Daily': 1,
            'Twice Daily': 2,
            'Three Times Daily': 3,
            'Four Times Daily': 4,
        }[prescription.frequency]

        # Check if the prescription has at least two dose times (for dose2_status)
        if num_dose_times >= 2:
            # Retrieve the Dose2Dispensation for the given date
            dispensation = Dose2Dispensation.objects.filter(
                prescription_id=prescription_id,
                dispensation_datetime__date=dispensation_date,
            ).last()

            if dispensation:
                dose2_status = getattr(dispensation, 'dose2_status', None)
                dispenser_name = dispensation.dispenser.username if dose2_status == 'Given' else None
            else:
                dose2_status = None
                dispenser_name = None

            # You can customize status_choices based on your model
            status_choices = [
                {'value': choice[0], 'label': choice[1]}
                for choice in Dose2Dispensation.TREATMENT_STATUS_CHOICES
            ]

            return JsonResponse({'dose2_status': dose2_status, 'dispenser_name': dispenser_name, 'status_choices': status_choices})

        else:
            return JsonResponse({'error': 'Prescription does not have at least two dose times.'}, status=400)

    except Prescription.DoesNotExist:
        return JsonResponse({'error': 'Prescription not found.'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_dose3_status(request, prescription_id, dispensation_date):
    try:
        prescription = Prescription.objects.get(id=prescription_id)
        # Calculate the number of dose times based on the selected frequency
        num_dose_times = {
            'Once Daily': 1,
            'Twice Daily': 2,
            'Three Times Daily': 3,
            'Four Times Daily': 4,
        }[prescription.frequency]

        # Check if the prescription has at least one dose time (for dose3_status)
        if num_dose_times >= 3:
            # Retrieve the Dose3Dispensation for the given date
            dispensation = Dose3Dispensation.objects.filter(
                prescription_id=prescription_id,
                dispensation_datetime__date=dispensation_date,
            ).last()

            if dispensation:
                dose3_status = getattr(dispensation, 'dose3_status', None)
                dispenser_name = dispensation.dispenser.username if dose3_status == 'Given' else None
            else:
                dose3_status = None
                dispenser_name = None

            # You can customize status_choices based on your model
            status_choices = [
                {'value': choice[0], 'label': choice[1]}
                for choice in Dose3Dispensation.TREATMENT_STATUS_CHOICES
            ]

            return JsonResponse({'dose3_status': dose3_status, 'dispenser_name': dispenser_name, 'status_choices': status_choices})

        else:
            return JsonResponse({'error': 'Prescription does not have at least three dose times.'}, status=400)

    except Prescription.DoesNotExist:
        return JsonResponse({'error': 'Prescription not found.'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_dose4_status(request, prescription_id, dispensation_date):
    try:
        prescription = Prescription.objects.get(id=prescription_id)
        # Calculate the number of dose times based on the selected frequency
        num_dose_times = {
            'Once Daily': 1,
            'Twice Daily': 2,
            'Three Times Daily': 3,
            'Four Times Daily': 4,
        }[prescription.frequency]

        # Check if the prescription has at least one dose time (for dose4_status)
        if num_dose_times >= 4:
            # Retrieve the Dose4Dispensation for the given date
            dispensation = Dose4Dispensation.objects.filter(
                prescription_id=prescription_id,
                dispensation_datetime__date=dispensation_date,
            ).last()

            if dispensation:
                dose4_status = getattr(dispensation, 'dose4_status', None)
                dispenser_name = dispensation.dispenser.username if dose4_status == 'Given' else None
            else:
                dose4_status = None
                dispenser_name = None

            # You can customize status_choices based on your model
            status_choices = [
                {'value': choice[0], 'label': choice[1]}
                for choice in Dose4Dispensation.TREATMENT_STATUS_CHOICES
            ]

            return JsonResponse({'dose4_status': dose4_status, 'dispenser_name': dispenser_name, 'status_choices': status_choices})

        else:
            return JsonResponse({'error': 'Prescription does not have at least four dose times.'}, status=400)

    except Prescription.DoesNotExist:
        return JsonResponse({'error': 'Prescription not found.'}, status=404)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def dose1_status_save_dispensation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            prescription_id = data.get('prescription_id')
            dose1_status = data.get('dose1_status')
            dispenser_id = request.user.id

            dispensation = Dose1Dispensation(
                prescription_id=prescription_id,
                dispenser_id=dispenser_id,
                dose1_status=dose1_status,
            )

            dispensation.save()

            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})

    return JsonResponse({'status': 'error'})

@csrf_exempt
def dose2_status_save_dispensation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            prescription_id = data.get('prescription_id')
            dose2_status = data.get('dose2_status')
            dispenser_id = request.user.id

            dispensation = Dose2Dispensation(
                prescription_id=prescription_id,
                dispenser_id=dispenser_id,
                dose2_status=dose2_status,
            )

            dispensation.save()

            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})

    return JsonResponse({'status': 'error'})

@csrf_exempt
def dose3_status_save_dispensation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            prescription_id = data.get('prescription_id')
            dose3_status = data.get('dose3_status')
            dispenser_id = request.user.id

            dispensation = Dose3Dispensation(
                prescription_id=prescription_id,
                dispenser_id=dispenser_id,
                dose3_status=dose3_status,
            )

            dispensation.save()

            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})

    return JsonResponse({'status': 'error'})

@csrf_exempt
def dose4_status_save_dispensation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            prescription_id = data.get('prescription_id')
            dose4_status = data.get('dose4_status')
            dispenser_id = request.user.id

            dispensation = Dose4Dispensation(
                prescription_id=prescription_id,
                dispenser_id=dispenser_id,
                dose4_status=dose4_status,
            )

            dispensation.save()

            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})

    return JsonResponse({'status': 'error'})
