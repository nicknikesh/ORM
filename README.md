# Ex02 Django ORM Web Application
## Date: 29.02.2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![alt text](<vijay/web application.png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 booksglo

## PROGRAM

```
Models.py

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

Admin.py

from django.contrib import admin
from .models import Bank ,BankAdmin
admin.site.register(Bank,BankAdmin)

```

## OUTPUT
![alt text](<Screenshot 2024-05-22 130855.png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
