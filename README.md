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
![Screenshot 2024-03-16 215259](https://github.com/nicknikesh/ORM/assets/145633284/9131de72-7788-44bb-9674-e0df07434352)
![Screenshot 2024-03-16 214222](https://github.com/nicknikesh/ORM/assets/145633284/c5939a56-2d67-44dc-b0c4-0628649b323f)







## RESULT
Thus the program for creating a database using ORM hass been executed successfully
