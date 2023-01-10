from django.db import models
#{"name": "Сибирская котята, 3 месяца", "author": "Павел", "price": 2500, "description": "Продаю", "address": "Москва, м. Студенческая", "is_published": true}


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=300)
    is_published = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True) # unique=True означает что одинаковых не будет, только уникальные

# чтобы наполнить таблицу файлами .csv нужно в терминале прописать python manage.py loaddata data\НАЗВАНИЕ_ФАЙЛА.json
#(домашка_27_django) PS C:\домашка_27_django> python manage.py loaddata data\ads.json
#Installed 20 object(s) from 1 fixture(s)
#(домашка_27_django) PS C:\домашка_27_django> python manage.py loaddata data\categories.json
#Installed 5 object(s) from 1 fixture(s)
