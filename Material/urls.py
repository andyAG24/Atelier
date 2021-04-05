from django.urls import path
from django.conf.urls import include
from .views import all_materials, view_material

urlpatterns = [
    path('', all_materials, name='all_materials'),
    path('view/<id>', view_material, name='view_material'),
    path('categories/', include('MaterialCategory.urls')),
]
