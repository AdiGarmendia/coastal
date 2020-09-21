# Generated by Django 3.0.9 on 2020-09-21 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coastalapp', '0002_remove_department_department_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='coastalapp.Employee'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='coastalapp.Department'),
        ),
    ]
