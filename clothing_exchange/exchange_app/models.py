from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TYPEofINSTITUTION = (
    (1, 'FUNACJA'),
    (2, 'ORGANIZACJA POZARZĄDOWA'),
    (3, 'ZBIÓRKA LOKALNA')
)


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)


class Institution(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(choices=TYPEofINSTITUTION, default=1)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=255)
    address_2 = models.PositiveIntegerField()
    phonenumber = models.IntegerField(max_length=9)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateTimeField(null=True)
    pick_up_time = models.DateTimeField(null=True)
    pick_up_comment = models.CharField(max_length=255)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
