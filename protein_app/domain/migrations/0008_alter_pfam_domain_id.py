# Generated by Django 4.0.10 on 2023-08-11 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0007_domain_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pfam',
            name='domain_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
