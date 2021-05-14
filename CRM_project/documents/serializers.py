import datetime

from django.contrib.auth.models import Group
from django.utils import timezone
from rest_framework.exceptions import ValidationError

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

    def create(self, validated_data):
        user = validated_data.pop('user')
        group = user.groups.all()[0].name
        doc_root = validated_data['document_root']
        if group == 'general' and doc_root in ['public', 'private', 'secret']:
            document = Document.objects.create(**validated_data)
        elif group == 'president':
            document = Document.objects.create(**validated_data)
        else:
            raise ValidationError("You have no permission!")
        return document
