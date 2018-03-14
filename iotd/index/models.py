from django.db import models
from django.utils import timezone
from rest_framework import viewsets


'''
  write your Model

class People(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    properties = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    num = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=255, blank=True, null=True)
    polynm = models.CharField(max_length=255, blank=True, null=True)
    orignm = models.CharField(max_length=255, blank=True, null=True)
    bthday = models.CharField(max_length=255, blank=True, null=True)
    properties2 = models.TextField(blank=True, null=True)
    hoovalsix = models.CharField(max_length=255, blank=True, null=True)
    hoopersix = models.CharField(max_length=255, blank=True, null=True)
    imaddr = models.CharField(max_length=255, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    email2 = models.CharField(max_length=255, blank=True, null=True)
    emaill = models.CharField(max_length=255, blank=True, null=True)
    perank = models.IntegerField(blank=True, null=True)
    secretary = models.TextField(blank=True, null=True)
    secretary2 = models.TextField(blank=True, null=True)
    electionnum = models.TextField(blank=True, null=True)
    reelegbnnm = models.TextField(blank=True, null=True)
    homep = models.TextField(blank=True, null=True)
    staff = models.TextField(blank=True, null=True)
    shrtnm = models.TextField(blank=True, null=True)
    memtitle = models.TextField(blank=True, null=True)
    examcd = models.TextField(blank=True, null=True)
    hbbycd = models.TextField(blank=True, null=True)
    keyword1 = models.TextField(blank=True, null=True)
    keyword2 = models.TextField(blank=True, null=True)
    keyword3 = models.TextField(blank=True, null=True)
    star = models.TextField(blank=True, null=True)
    freepartycount = models.TextField(blank=True, null=True)
    bthplace = models.TextField(blank=True, null=True)
    hoovalseven = models.TextField(blank=True, null=True)
    hooperseven = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'people'

'''

