# Generated by Django 4.0.4 on 2022-06-12 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domain',
            name='description',
        ),
    ]
