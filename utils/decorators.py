from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse


def permission_checker_decorator_factory(data=None):
    def permission_checker_decorator(func):
        def wrapper(request: HttpRequest, *args, **kwargs):
            if request.user.is_authenticated:
                return func(request, *args, **kwargs)
            else:
                return redirect(reverse('login_page'))

        return wrapper

    return permission_checker_decorator


def is_login_decorator(data=None):
    def login_checker_decorator(func):
        def wrapper(request: HttpRequest, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(reverse('home_page'))
            else:
                return func(request, *args, **kwargs)

        return wrapper

    return login_checker_decorator
