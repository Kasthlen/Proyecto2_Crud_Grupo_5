from django.urls import path
from .views import (
    ServiceListCreate, ServiceRetrieveUpdateDestroy, 
    ServiceCategoryListCreate, ServiceCategoryRetrieveUpdateDestroy,
    VistaAdmin, VistaEditor
)

urlpatterns = [
    path('', ServiceListCreate.as_view(), name='service-list-create'),
    path('<int:pk>/', ServiceRetrieveUpdateDestroy.as_view(), name='service-detail'),
    path('categories/', ServiceCategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', ServiceCategoryRetrieveUpdateDestroy.as_view(), name='category-detail'),

    path('solo-admin/', VistaAdmin.as_view(), name='solo-admin'),
    path('solo-editores/', VistaEditor.as_view(), name='solo-editores'),
]
