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
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    mark = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    year = models.DateField(auto_now_add=True)
    number = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    type = models.CharField(choices=choice, max_length=10)

    def __str__(self):
        return self.mark