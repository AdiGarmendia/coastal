# Generated by Django 3.0.9 on 2020-09-21 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coastalapp', '0003_auto_20200921_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='assigned_employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_employees', to='coastalapp.Employee'),
        ),
    ]
