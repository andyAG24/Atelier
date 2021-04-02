from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse(_('You are not allowed to view this page.'))
        return wrapper_func
    return decorator

def template(template):
    def wrapper(view):
        def call(request, *args, **kwargs):
            context = {}
            ret = view(request, context, *args, **kwargs)
            if ret: 
                return(ret)
            return render(template, RequestContext(request, context))
        return call
    return wrapper

