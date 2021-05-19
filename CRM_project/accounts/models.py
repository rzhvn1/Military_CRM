from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Dossier(models.Model):
    gender_choices = (
        ("M", "M"),
        ("F", "F")
    )
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=100)
    date_birth = models.DateField()
    image = models.ImageField(blank=True, null=True)
    gender = models.CharField(choices=gender_choices, max_length=10)

    def __str__(self):
        return self.full_name

class Car(models.Model):
    choice = (
        ('State', 'State'),
        ('Private', 'Private'),
    )
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='cars')
    mark = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    number = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    type = models.CharField(choices=choice, max_length=10)

    def __str__(self):
        return self.mark

class Education(models.Model):
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='educations')
    start_date = models.DateField()
    end_date = models.DateField()
    school_name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)


class Warcraft(models.Model):
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='warcrafts')
    start_date = models.DateField()
    end_date = models.DateField()
    military_area = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    start_pose = models.CharField(max_length=100)
    end_pose = models.CharField(max_length=100)

