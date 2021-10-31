# Generated by Django 3.2.8 on 2021-10-22 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.IntegerField(choices=[(1, 'FUNACJA'), (2, 'ORGANIZACJA POZARZĄDOWA'), (3, 'ZBIÓRKA LOKALNA')], default=1)),
                ('categories', models.ManyToManyField(to='exchange_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.PositiveIntegerField()),
                ('phonenumber', models.IntegerField()),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=6)),
                ('pick_up_date', models.DateTimeField(null=True)),
                ('pick_up_time', models.DateTimeField(null=True)),
                ('pick_up_comment', models.CharField(max_length=255)),
                ('categories', models.ManyToManyField(to='exchange_app.Category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange_app.institution')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
