# Generated by Django 4.0.4 on 2022-06-22 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protein', '0006_alter_protein_domains_alter_protein_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='protein',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
