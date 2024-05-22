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
class Book(models.Model):
bookid=models.IntegerField(primary_key=True);
bookname=models.CharField(max_length=20);
author=models.CharField(max_length=50);
price=models.IntegerField();
publishdate=models.DateField();
class BookAdmin(admin.ModelAdmin):
list_display=("bookid","bookname","author","price","publishdate");

Admin.py

from django.contrib import admin
from .models import Book ,BookAdmin
admin.site.register(Book,BookAdmin)

```

## OUTPUT
![Screenshot 2024-05-22 135443](https://github.com/nicknikesh/ORM/assets/145633284/3ebeb1da-07bd-476a-9e0a-5167acb041ea)
![Screenshot 2024-05-22 135520](https://github.com/nicknikesh/ORM/assets/145633284/9ff1e7b5-8459-493a-91ef-e42947bbcceb)






## RESULT
Thus the program for creating a database using ORM hass been executed successfully
