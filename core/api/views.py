from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import Companyserializer, Employeeserializer


# Create your views here.
class Companyviewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = Companyserializer

#creating employee viewset
class Employeeviewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer