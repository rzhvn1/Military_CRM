from django.db import models

# Create your models here.
class Document(models.Model):
    choice = (
        ('active', 'active'),
        ('dead', 'dead')
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    file = models.FileField(blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_expired = models.DateField()
    status = models.CharField(choices=choice, max_length=10, default='active')
    document_root = models.CharField(choices=(
        ('public', 'public'),
        ('private', 'private'),
        ('secret', 'secret'),
        ('top-secret', 'top-secret'),
    ),max_length=100)