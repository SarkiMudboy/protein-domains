# Generated by Django 4.0.4 on 2022-06-16 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0004_remove_domain_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pfam',
            name='domain_description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='pfam',
            name='domain_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
