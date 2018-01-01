# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

Context_for_year = (
    (0,"None"),
	(1,"First"),
	(2,"Second"),
	(3,"Third"),
	(4,"Fourth"),
	(5,"Fifth")
	)

class Users(models.Model):
    UserName = models.CharField(verbose_name='UserName',max_length=254,null=True,blank=True)
    Year = models.IntegerField(null=False,choices=Context_for_year,default=0)
    Rollno = models.CharField(null=False,max_length=9,default="none")
    Email = models.EmailField(verbose_name='Email',max_length=254,primary_key=True)
    Phone = models.CharField(verbose_name='Phone Number',max_length=254,null=True,blank=True)

    class Meta:
        unique_together = ('UserName', 'Email')

    def __str__(self):
        return "{},{},{}".format(self.Email,self.UserName,self.Rollno)
        
