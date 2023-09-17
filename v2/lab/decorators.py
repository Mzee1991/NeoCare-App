from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect

def custom_user_passes_test(test_func, error_page=None, permission_denied_message=None):
    """
    Custom user_passes_test decorator that redirects the user to an error page when
    the test fails.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not test_func(request.user):
                if error_page:
                    return render(request, error_page)
                else:
                    # Return a default error response, or customize as needed
                    return HttpResponse("Permission Denied", status=403)
            return view_func(request, *args, **kwargs)
        
        return _wrapped_view

    return decorator

lab_tech_required = custom_user_passes_test(
    lambda u: u.groups.filter(name='Lab Tech').exists(),
    error_page='lab/error_page.html',  # Provide the path to your error page template
)
