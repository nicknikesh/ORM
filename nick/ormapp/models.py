from django.db import models
from django.contrib import admin
class Bank(models.Model):
     accountno=models.IntegerField(primary_key=True);
     cardholdername=models.CharField(max_length=20);
     branch=models.CharField(max_length=50);
     depositedammount=models.IntegerField();
     accountopendate=models.DateField();
class BankAdmin(admin.ModelAdmin):
     list_display=("accountno","cardholdername","branch","depositedammount","accountopendate");