from rest_framework import serializers
from api.models import Company
# creating comapny serializers
class Companyserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        
        