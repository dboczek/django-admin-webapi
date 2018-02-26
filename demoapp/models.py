# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

CHOICES1 = (
    ('A', 'Alpha'),
    ('B', 'Beta'),
)


class TestModel1(models.Model):
    boolean = models.BooleanField(default=True)
    char = models.CharField(max_length=15)
    choices1 = models.CharField(max_length=1, choices=CHOICES1)
    date = models.DateField()
    datetime = models.DateTimeField()
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()
    email = models.EmailField()
    float = models.FloatField()
    integer = models.IntegerField()
    text = models.TextField()
    time = models.TimeField()
    url = models.URLField()


# class TestModel2(models.Model)
#     char = models.CharField()
#     file = models.FileField()


# class TestMdodel3(models.Model)
#     char = models.CharField()
#     filepath = models.FilePathField(path='/home/daniel/blah')


# class TestModel4(models.Model)
#     char = models.CharField()
#     image = models.ImageField()


# class TestModel5(models.Model):
#     genericipaddress = models.GenericIPAddressField()
#     nullboolean = models.NullBooleanField()
#     positiveinteger = models.PositiveIntegerField()
#     positivesmallinteger = models.PositiveSmallIntegerField()
#     slugfield = models.SlugField()
#     smallinteger = models.SmallIntegerField()
#     uuid = models.UUIDField()
#     auto = models.AutoField()
#     bigauto = models.BigAutoField()
#     biginteger = models.BigIntegerField()
#     binary = models.BinaryField()
