from django.contrib import admin
from .models import Dossier, Car, Education, Warcraft
# Register your models here.
admin.site.register([Dossier, Car, Education, Warcraft])
