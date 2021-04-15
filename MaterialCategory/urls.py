from django.urls import path
from django.conf.urls import include
from .views import all_categories, view_category, add_category, delete_category, EditMaterialCategoryView

urlpatterns = [
    path('', all_categories, name='all_categories'),
    path('view/<id>', view_category, name='view_category'),
    path('add', add_category, name='add_category'),
    path('delete/<id>', delete_category, name='delete_category'),
    path('edit/<int:pk>', EditMaterialCategoryView.as_view(), name='edit_material_category'),
]
