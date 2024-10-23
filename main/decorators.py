from django.shortcuts import redirect
from django.urls import reverse
from functools import wraps

def check_payment(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Assuming the 'permit' field is in the User model
            if not request.user.permit:
                return redirect(reverse('permit'))  # Redirect to your payment page
        return view_func(request, *args, **kwargs)
    return _wrapped_view
