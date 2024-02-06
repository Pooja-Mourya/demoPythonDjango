from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Car(models.Model):
    car_name = models.CharField(max_length=22)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return self.car
