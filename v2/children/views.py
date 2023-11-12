from .forms import RegistrationForm, MeasurementsForm, LabRequestChildrenForm
from .models import Registration, LabRequestChildren, LabResultChildren
from newborn.forms import MotherLocationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django import template
from datetime import date
from django.utils import timezone

@login_required
def child_registration(request):
    if request.method == 'POST':
        location_form = MotherLocationForm(request.POST)
        registration_form = RegistrationForm(request.POST)

        if location_form.is_valid() and registration_form.is_valid():
            location_instance = location_form.save(commit=False)
            location_instance.save()

            registration_instance = registration_form.save(commit=False)
            registration_instance.location = location_instance
            registration_instance.registered_by = request.user
            registration_instance.save()

            # Rest of your code to save the instances and redirect
            return redirect('home-page')

    else:
        registration_form = RegistrationForm()
        location_form = MotherLocationForm(is_update=False)

    context = {
        'registration_form': registration_form,
        'location_form': location_form,
    }

    return render(request, 'children/child_registration_form.html', context)

def child_information(request, child_id):
    child = get_object_or_404(Registration, pk=child_id)
    
    # Calculate age in years and months
    today = date.today()
    age = today.year - child.date_of_birth.year - ((today.month, today.day) < (child.date_of_birth.month, child.date_of_birth.day))

    # Calculate the number of months as the remainder
    months = (today.year - child.date_of_birth.year) * 12 + today.month - child.date_of_birth.month
    remaining_months = months % 12

    context = {'child': child, 'age_years': age, 'age_months': remaining_months}
    return render(request, 'children/child_information.html', context)


def record_measurements(request, registration_id):
    registration = get_object_or_404(Registration, pk=registration_id)

    if request.method == 'POST':
        form = MeasurementsForm(request.POST)
        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.registration = registration
            measurement.save()
            return redirect(reverse('child_information', kwargs={'pk': registration_id}))  # Redirect to a success page after successfully recording the measurements
    else:
        form = MeasurementsForm()
    return render(request, 'children/record_measurements.html', {'form': form, 'registration': registration})


@login_required
def children_lab_request(request, child_id):
    child = get_object_or_404(Registration, pk=child_id)

    if request.method == 'POST':
        form = LabRequestChildrenForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.child = child
            instance.author = request.user
            instance.timestamp = timezone.now()

            # Set the specific test fields to True based on user selection
            instance.serum_electrolytes_requested = form.cleaned_data.get('serum_electrolytes_requested', False)
            instance.serum_bilirubin_requested = form.cleaned_data.get('serum_bilirubin_requested', False)
            instance.serum_ast_requested = form.cleaned_data.get('serum_ast_requested', False)
            instance.serum_alt_requested = form.cleaned_data.get('serum_alt_requested', False)
            instance.serum_alp_requested = form.cleaned_data.get('serum_alp_requested', False)
            instance.serum_urea_requested = form.cleaned_data.get('serum_urea_requested', False)
            instance.serum_creatinine_requested = form.cleaned_data.get('serum_creatinine_requested', False)
            instance.complete_blood_count_requested = form.cleaned_data.get('complete_blood_count_requested', False)
            instance.blood_grouping_requested = form.cleaned_data.get('blood_grouping_requested', False)
            instance.peripheral_thin_film_requested = form.cleaned_data.get('peripheral_thin_film_requested', False)
            instance.blood_smear_requested = form.cleaned_data.get('blood_smear_requested', False)
            instance.urinalysis_requested = form.cleaned_data.get('urinalysis_requested', False)
            instance.stool_analysis_requested = form.cleaned_data.get('stool_analysis_requested', False)
            instance.h_pylori_stool_antigen_test_requested = form.cleaned_data.get('h_pylori_stool_antigen_test_requested', False)
            instance.antistreptolysin_test_requested = form.cleaned_data.get('antistreptolysin_test_requested', False)
            instance.hepatitis_b_surface_antigen_requested = form.cleaned_data.get('hepatitis_b_surface_antigen_requested', False)
            instance.malaria_rdts_requested = form.cleaned_data.get('malaria_rdts_requested', False)
            instance.rbs_requested = form.cleaned_data.get('rbs_requested', False)
            instance.rct_requested = form.cleaned_data.get('rct_requested', False)
            instance.rpr_requested = form.cleaned_data.get('rpr_requested', False)
            instance.sickling_test_requested = form.cleaned_data.get('sickling_test_requested', False)

            instance.save()
            return redirect(reverse('child_information', kwargs={'child_id': child_id}))
    else:
        form = LabRequestChildrenForm()

    return render(request, 'children/children_lab_request.html', {'form': form, 'child': child})


def pending_tests_for_child(request, child_id):
    # Get the child's registration information
    child = Registration.objects.get(pk=child_id)

    # Get pending lab test requests for the child
    pending_lab_requests = LabRequestChildren.objects.filter(child=child)

    context = {
        'child': child,
        'pending_lab_requests': pending_lab_requests,
    }

    return render(request, 'children/pending_tests.html', context)