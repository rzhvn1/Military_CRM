from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from .models import *
from .serializers import DossierSerializer, RegisterSerializer, CarSerializer, EducationSerializer, WarcraftSerializer
from rest_framework import viewsets

# Create your views here.

class DossierModelViewSet(viewsets.ModelViewSet):
    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer