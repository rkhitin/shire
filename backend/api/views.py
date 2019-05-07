from rest_framework import viewsets
from .models import Customer, Habbit
from .serializers import CustomerSerializer, HabbitSerrializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class HabbitViewSet(viewsets.ModelViewSet):
    queryset = Habbit.objects.all()
    serializer_class = HabbitSerrializer
