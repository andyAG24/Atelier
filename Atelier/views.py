from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from .decorators import template
# from Employee.models import Employee
from .decorators import unauthenticated_user, allowed_users

@login_required(login_url='auth')
@allowed_users(allowed_roles=['Managers', 'Sewers'])
def mainpage_view(request):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name
    return render(request, 'main.html', context)

@unauthenticated_user
def redirect_to_auth(request):
    return render(request, 'registration/login.html')
