from rest_framework import serializers
from api.models import Company, Employee


# creating comapny serializers
class Companyserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        
#creating employeeserializer
class Employeeserializer(serializers.HyperlinkedModelSerializer):
    Employee_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"

