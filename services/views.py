import logging
logger = logging.getLogger('services')

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Service, ServiceCategory
from .serializers import ServiceSerializer, ServiceCategorySerializer, ServiceListSerializer

class ServiceCategoryListCreate(generics.ListCreateAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    ordering = ['name']
def get(self, request, *args, **kwargs):                 # ← NUEVA línea 13
        logger.info("Se consultaron las categorías de servicio") # ← NUEVA línea 14
        return super().get(request, *args, **kwargs)          # ← NUEVA línea 15

class ServiceCategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer

class ServiceListCreate(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    filterset_fields = ['name', 'category', 'is_active']
    search_fields = ['name', 'code', 'description']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'price', 'created_at']
    ordering = ['name']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ServiceListSerializer
        return ServiceSerializer

class ServiceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer