# Generated by Django 3.2 on 2021-05-04 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_dossier_date_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='dossier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='accounts.dossier'),
        ),
    ]