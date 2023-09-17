from treatment.models import Dose1Dispensation, Dose2Dispensation, Dose3Dispensation, Dose4Dispensation, Prescription
from newborn.models import NewbornAdmission
from treatment.forms import PrescriptionForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date, timedelta, datetime
from django.utils.timesince import timesince
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
import json

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
    print(admission)
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
    print(prescriptions)
    print("leave a line")


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

    return render(request, 'treatment/prescription.html', context)


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

    return render(request, 'treatment/prescription.html')



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
