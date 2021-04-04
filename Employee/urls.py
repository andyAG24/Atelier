from django.urls import path
from django.conf.urls import include
from .views import all_employees, view_employee

urlpatterns = [
    # path('auth/', redirect_to_auth, name='auth'),
    path('', all_employees, name='all_employees'),
    path('view/<id>', view_employee, name='view_employee'),

    # path('categories/', include('MaterialCategory.urls')),
]
