from django.urls import path
from .views import all_materials, view_material

urlpatterns = [
    # path('auth/', redirect_to_auth, name='auth'),
    path('', all_materials, name='all_materials'),
    path('view/<id>', view_material, name='view_material')
]
