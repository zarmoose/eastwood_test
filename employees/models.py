from django.db import models
from phone_field import PhoneField


# Create your models here.
class Employee(models.Model):
    class Meta:
        db_table = "employee"

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    email = models.EmailField()
    phone = PhoneField(blank=True)
    begin_work = models.DateField()
    end_work = models.DateField()
    position = models.CharField(max_length=200)