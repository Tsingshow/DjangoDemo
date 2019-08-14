# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Person(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    birth = models.CharField(max_length=128)