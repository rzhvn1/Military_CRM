from datetime import datetime

from django.db import transaction

from .services import mailing, validate_password
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *
from django.utils import timezone

class WarcraftSerializer(serializers.ModelSerializer):

    warcraft_id = serializers.IntegerField(source='id', required=False)

    class Meta:
        model = Warcraft
        fields = ['warcraft_id', 'start_date', 'end_date', 'military_area', 'major', 'start_pose', 'end_pose']

class EducationSerializer(serializers.ModelSerializer):

    education_id = serializers.IntegerField(source='id', required=False)

    class Meta:
        model = Education
        fields = ['education_id', 'start_date', 'end_date', 'school_name', 'major']


class CarSerializer(serializers.ModelSerializer):

    car_id = serializers.IntegerField(source='id', required=False)

    class Meta:
        model = Car
        fields = ['car_id', 'mark', 'car_model', 'year', 'number', 'color', 'type']

class DossierSerializer(serializers.ModelSerializer):

    cars = CarSerializer(many=True)
    educations = EducationSerializer(many=True)
    warcrafts = WarcraftSerializer(many=True)


    class Meta:
        model = Dossier
        fields = ['id', 'full_name', 'date_birth', 'gender', 'image', 'cars', 'educations', 'warcrafts']

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name',instance.full_name)
        cars_data = validated_data.pop('cars')
        educations_data = validated_data.pop('educations')
        warcrafts_data = validated_data.pop('warcrafts')
        ids_list_car = [car.id for car in instance.cars.all()]
        currents_ids_car = [car['id'] for car in cars_data]
        final_list_car = [car_id for car_id in ids_list_car if car_id not in currents_ids_car]

        ids_list_education = [education.id for education in instance.educations.all()]
        currents_ids_education = [education['id'] for education in educations_data]
        final_list_education = [education_id for education_id in ids_list_education if education_id not in currents_ids_education]

        ids_list_warcraft = [warcraft.id for warcraft in instance.warcrafts.all()]
        currents_ids_warcraft = [warcraft['id'] for warcraft in warcrafts_data]
        final_list_warcraft = [warcraft_id for warcraft_id in ids_list_warcraft if warcraft_id not in currents_ids_warcraft]
        for car in cars_data:
            car_id = car['id']
            car_data = Car.objects.get(id=car_id)
            for delete_id in final_list_car:
                delete_car = Car.objects.get(id=delete_id)
                delete_car.delete()
            car_data.mark = car['mark']
            car_data.car_model = car['car_model']
            car_data.year = car['year']
            car_data.number = car['number']
            car_data.color = car['color']
            car_data.type = car['type']
            car_data.save()
        for education in educations_data:
            education_id = education['id']
            education_data = Education.objects.get(id=education_id)
            for delete_id in final_list_education:
                delete_education = Education.objects.get(id=delete_id)
                delete_education.delete()
            education_data.school_name = education['school_name']
            education_data.start_date = education['start_date']
            education_data.end_date = education['end_date']
            education_data.major = education['major']
            education_data.save()
        for warcraft in warcrafts_data:
            warcraft_id = warcraft['id']
            warcraft_data = Warcraft.objects.get(id=warcraft_id)
            for delete_id in final_list_warcraft:
                delete_warcraft = Warcraft.objects.get(id=delete_id)
                delete_warcraft.delete()
            warcraft_data.military_area = warcraft['military_area']
            warcraft_data.start_date = warcraft['start_date']
            warcraft_data.end_date = warcraft['end_date']
            warcraft_data.major = warcraft['major']
            warcraft_data.start_pose = warcraft['start_pose']
            warcraft_data.end_pose = warcraft['end_pose']
            warcraft_data.save()
        instance.save()
        return instance



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

    @transaction.atomic
    def create(self, validated_data):
        user_type = validated_data.pop('user_type')
        password = validated_data.pop('password')
        check_password = validated_data.pop('check_password')
        dossier_data = validated_data.pop('dossier')
        user = User.objects.create(**validated_data)
        if password == check_password:
            validated_password = validate_password(password)
            if validated_password == True:
                print("Validated Password!")
            else:
                raise ValidationError("Your password must follow these 5 rules:"
    "1) Your password must be 8 or more than 8 characters"
    "2) Your password must contain at least one uppercase, or capital, letter (ex: A, B, etc.)"
    "3) Your password must contain at least one lowercase letter."
    "4) Your password must contain at least one number digit (ex: 0, 1, 2, 3, etc.)"
    "5) Your password must not contain spaces between the letters or digits")
        else:
            raise ValidationError("Passwords don't match")
        user.set_password(password)
        if user_type == 'military':
            user.is_active = False
            group = Group.objects.get(name='sergeant')
            user.groups.add(group)
            mailing(user.username)
        user.save()
        cars_data = dossier_data.pop('cars')
        educations_data = dossier_data.pop('educations')
        warcrafts_data = dossier_data.pop('warcrafts')
        dossier = Dossier.objects.create(user=user, **dossier_data)

        for car in cars_data:
            Car.objects.create(dossier=dossier, **car)

        for education in educations_data:
            Education.objects.create(dossier=dossier, **education)

        for warcraft in warcrafts_data:
            Warcraft.objects.create(dossier=dossier, **warcraft)
        return user





