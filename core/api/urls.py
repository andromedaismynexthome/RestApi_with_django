from django.contrib import admin
from django.urls import path,include
from api.views import Companyviewset
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'companies', Companyviewset)

urlpatterns = [
  path('',include(router.urls))
]
