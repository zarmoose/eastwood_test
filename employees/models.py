from django.db import models
from django.db.models import SET_NULL
from phone_field import PhoneField


# Create your models here.
class Department(models.Model):
    """Отдел компании"""

    class Meta:
        db_table = "department"

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Сотрудник компании"""

    class Meta:
        db_table = "employee"

    first_name = models.CharField('Имя', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    birthday = models.DateField('Дата рождения')
    email = models.EmailField('e-mail')
    phone = PhoneField('Телефон', blank=True)
    begin_work = models.DateField('Начало работы')
    end_work = models.DateField('Окончание работы', blank=True, null=True)
    position = models.CharField('Должность', max_length=200)
    department = models.ForeignKey(Department, on_delete=SET_NULL, blank=True, null=True)

    def __str__(self):
        return ' '.join((self.last_name, self.first_name, self.middle_name, ))
