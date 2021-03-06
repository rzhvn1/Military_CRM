# Generated by Django 3.2 on 2021-04-28 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=100)),
                ('year', models.DateField(auto_now_add=True)),
                ('number', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('State', 'State'), ('Private', 'Private')], max_length=10)),
                ('dossier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.dossier')),
            ],
        ),
    ]
