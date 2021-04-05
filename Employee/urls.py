from django.urls import path
from .views import all_employees, view_employee, view_own_profile

urlpatterns = [
    path('', all_employees, name='all_employees'),
    path('view/<id>', view_employee, name='view_employee'),
    path('own_profile', view_own_profile, name='view_own_profile'),
]
