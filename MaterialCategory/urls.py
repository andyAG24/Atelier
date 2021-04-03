from django.urls import path
from django.conf.urls import include
from .views import all_categories, view_category

urlpatterns = [
    path('', all_categories, name='all_categories'),
    path('view/<id>', view_category, name='view_category'),
]
