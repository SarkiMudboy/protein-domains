# Generated by Django 3.2.3 on 2022-05-31 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pfam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_id', models.CharField(max_length=10)),
                ('domain_description', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField(default=0)),
                ('stop', models.IntegerField(default=0)),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='protein_sequence_domain_description', to='domain.pfam', to_field='domain_description')),
                ('pfam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.pfam')),
            ],
        ),
    ]
