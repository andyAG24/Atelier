from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import template
# from Employee.models import Employee
from .decorators import unauthenticated_user, allowed_users

@login_required(login_url='auth')
@allowed_users(allowed_roles=['Managers', 'Sewers'])
def mainpage_view(request):
    context = {}
    # context = {'kek': 'kek'}
    # render_menu(request)
    
    context['user_group'] = request.user.groups.all()[0].name
    return render(request, 'main.html', context)

@unauthenticated_user
def redirect_to_auth(request):
    print('kek')
    return render(request, 'registration/login.html')

# def is_user_in_group(request, group_name):
#     print('works')
#     user_group = request.user.groups.all()[0].name
#     if user_group == group_name:
#         return 'True'
#     else:
#         return 'False'

# @template('header')
# def header(request, context):
#     context['user_group'] = request.user.groups.all()[0].name
#     context['userr'] = request.user.groups.filter(name='Instructors').exists()
