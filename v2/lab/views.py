from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .forms import LabTestRequestForm, DynamicLabResultForm
from .models import LabRequest, LabResult
from newborn.models import NewbornAdmission
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .decorators import lab_tech_required


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

    return render(request, 'lab/lab_request2.html', {'form': form})


@login_required
@lab_tech_required
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
    return render(request, 'lab/lab_requests_dashboard.html', context)


@lab_tech_required
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
    return render(request, 'lab/input_lab_results.html', context)


@lab_tech_required
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
    return render(request, 'lab/pending_lab_tests.html', context)
