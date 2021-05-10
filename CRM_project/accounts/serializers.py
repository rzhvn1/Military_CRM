from datetime import datetime
from .services import mailing
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *
from django.utils import timezone

class WarcraftSerializer(serializers.ModelSerializer):


    class Meta:
        model = Warcraft
        fields = ['id', 'start_date', 'end_date', 'military_area', 'major', 'start_pose', 'end_pose']

class EducationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Education
        fields = ['id', 'start_date', 'end_date', 'school_name', 'major']


class CarSerializer(serializers.ModelSerializer):


    class Meta:
        model = Car
        fields = ['id', 'mark', 'car_model', 'year', 'number', 'color', 'type']

class DossierSerializer(serializers.ModelSerializer):

    cars = CarSerializer(many=True)
    educations = EducationSerializer(many=True)
    warcrafts = WarcraftSerializer(many=True)


    class Meta:
        model = Dossier
        fields = ['id', 'user', 'full_name', 'date_birth', 'gender', 'image', 'cars', 'educations', 'warcrafts']

    def create(self, validated_data):
        cars_data = validated_data.pop('cars')
        educations_data = validated_data.pop('educations')
        warcrafts_data = validated_data.pop('warcrafts')
        dossier = Dossier.objects.create(**validated_data)
        for car in cars_data:
            Car.objects.create(dossier=dossier, **car)
        for education in educations_data:
            Education.objects.create(dossier=dossier, **education)
        for warcraft in warcrafts_data:
            Warcraft.objects.create(dossier=dossier, **warcraft)
        return dossier



class RegisterSerializer(serializers.ModelSerializer):
    check_password = serializers.CharField(write_only=True)
    user_type = serializers.ChoiceField(choices=(
        ('common', 'commom'),
        ('military', 'military')
    ), write_only=True)
    dossier = DossierSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'check_password', 'user_type', 'dossier']

    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        password = validated_data.pop('password')
        check_password = validated_data.pop('check_password')
        user = User.objects.create(**validated_data)
        if password != check_password:
            raise ValidationError("Passwords don't match")
        user.set_password(password)
        if user_type == 'military':
            user.is_active = False
            group = Group.objects.get(name='sergeant')
            user.groups.add(group)
            mailing(user.username)
        user.save()
        Dossier.objects.create(user=user)
        return user





