# Generated by Django 3.2.12 on 2023-03-01 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
        migrations.RemoveField(
            model_name='student',
            name='mobileno',
        ),
        migrations.RemoveField(
            model_name='student',
            name='pincode',
        ),
    ]
