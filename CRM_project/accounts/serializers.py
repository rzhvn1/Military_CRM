from datetime import datetime

from rest_framework import serializers
from .models import *
from django.utils import timezone

class DossierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dossier
        fields = ['id', 'user', 'full_name', 'date_birth', 'gender', 'image']



