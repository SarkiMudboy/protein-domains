# Generated by Django 4.0.4 on 2022-06-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0005_alter_pfam_domain_description_alter_pfam_domain_id'),
        ('protein', '0005_alter_taxa_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protein',
            name='domains',
            field=models.ManyToManyField(blank=True, null=True, to='domain.domain'),
        ),
        migrations.AlterField(
            model_name='protein',
            name='length',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
