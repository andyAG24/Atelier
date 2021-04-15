from django.urls import path
from django.conf.urls import include
from .views import all_materials, view_material, add_material, delete_material, EditMaterialView

urlpatterns = [
    path('', all_materials, name='all_materials'),

    path('view/<id>', view_material, name='view_material'),
    path('add', add_material, name='add_material'),
    path('delete/<id>', delete_material, name='delete_material'),
    path('edit/<int:pk>', EditMaterialView.as_view(), name='edit_material'),

    path('categories/', include('MaterialCategory.urls')),
]
