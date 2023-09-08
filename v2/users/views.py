from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from .forms import UserRegistrationForm
from .models import RegistrationRequest, UserProfile
from django.core.mail import send_mail
import uuid
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.decorators import user_passes_test
import secrets
import string
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('home-page')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'users/profile.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Capture form data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            group = form.cleaned_data['group']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            nin_no = form.cleaned_data['nin_no']
            contact = form.cleaned_data['contact']

            # Generate a unique token (you can use UUID or a random string generator)
            token = str(uuid.uuid4())

            try:
                with transaction.atomic():
                    # Create a User instance
                    user = User(username=username, email=email, first_name=first_name, last_name=last_name)
                    user.set_unusable_password()  # Set an unusable password
                    user.save()

                    # Create a UserProfile instance and associate it with the User
                    profile = UserProfile(user=user, nin_no=nin_no, contact=contact)
                    profile.save()

                    # Create a registration request without saving it to the database
                    registration = RegistrationRequest(
                        user=user,
                        group=group,
                        token=token,
                    )
                    registration.save()

                    # Send an email to the administrator with the approval link
                    approval_link = f'http://127.0.0.1:8000/approve_registration/{token}/'
                    send_mail(
                        'New Registration Request',
                        f'A new registration request has been submitted. Click the link to approve or reject: {approval_link}',
                        'yohanamariamzee@gmail.com',
                        ['yohanamariamzee@gmail.com'],  # Administrator's email
                        fail_silently=False,
                    )

                    messages.success(request, 'Your registration request has been submitted for approval.')
                    # Set the message in the session
                    request.session['registration_message'] = 'Your registration request has been submitted for approval.'
                                            
                    return redirect('registration-done')
            except Exception as e:
                # Handle any exceptions that may occur during the transaction
                messages.error(request, f'Error occurred during registration: {str(e)}')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def registration_done(request):
    # Retrieve the message from the session (set in the 'register' view)
    message = request.session.get('registration_message', '')
    
    return render(request, 'users/registration_done.html', {'message': message})

def generate_random_password(length=8):
    # Generate a random password using letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

@login_required
def approve_registration(request, token):
    try:
        registration = RegistrationRequest.objects.get(token=token)
    except RegistrationRequest.DoesNotExist:
        messages.error(request, 'Invalid registration request.')
        return redirect('home-page')

    if request.method == 'POST':
        # Check if the "approve" button was clicked
        if request.POST.get('action') == 'approve':
            # Get the existing user associated with the registration request
            user = registration.user

            # Retrieve the group object based on its name
            group_name = registration.group
            try:
                group = Group.objects.get(name=group_name)
            except Group.DoesNotExist:
                messages.error(request, f'Group "{group_name}" does not exist.')
                return redirect('home-page')

            # Add the user to the group
            user.groups.add(group)
            user.save()

            # Generate a random password for the user
            new_password = generate_random_password()

            # Set the new password for the user
            user.set_password(new_password)
            user.save()

            # Notify the user with their username and new password
            send_mail(
                'Account Approved',
                f'Your account has been approved. Your username: {user.username}, Your password: {new_password}',
                'yohanamariamzee@gmail.com',
                [registration.user.email],
                fail_silently=False,
            )

            messages.success(request, 'User account has been approved. Username and password sent to your email.')
        else:
            # Remove the user from the group
            try:
                user = registration.user
                group_name = registration.group
                group = Group.objects.get(name=group_name)
                user.groups.remove(group)
                user.delete()
            except ObjectDoesNotExist:
                pass

            # Notify the user about rejection
            send_mail(
                'Account Rejected',
                'Your registration request has been rejected.',
                'yohanamariamzee@gmail.com',
                [registration.user.email],
                fail_silently=False,
            )

        # Delete the registration request
        registration.delete()

        return redirect('home-page')

    return render(request, 'users/approve_registration.html', {'registration': registration})
