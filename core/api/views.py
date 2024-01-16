from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import Companyserializer, Employeeserializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class Companyviewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = Companyserializer

    # we creating custom urls companies/primarykey/employees
    @action(detail=True, methods=['get'])
    def employees(self,request,pk=None):
        try:

            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = Employeeserializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'comany might not exits'
            })



#creating employee viewset
class Employeeviewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer