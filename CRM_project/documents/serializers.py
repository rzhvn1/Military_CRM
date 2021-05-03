import datetime

from django.utils import timezone

from .models import *
from rest_framework import serializers

class DocumentSerializer(serializers.ModelSerializer):
    check_date = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ['id', 'title', 'text', 'file', 'date_created', 'date_expired', 'status', 'document_root', 'check_date']


    def get_check_date(self, obj):
        check_date = ''
        date_expired = obj.date_expired
        date_now = datetime.datetime.date(timezone.now())
        if date_now > date_expired:
            check_date = 'dead'
            obj.status = check_date
            obj.save()
        return check_date
