from django.db import models
from phone_field import PhoneField


# Create your models here.
class Department(models.Model):
    """Отдел компании"""

    name = models.CharField(verbose_name="Название отдела", max_length=200)

    class Meta:
        db_table = 'department'
        ordering = ['name']

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Сотрудник компании"""

    first_name = models.CharField(verbose_name="Имя", max_length=50)
    middle_name = models.CharField(verbose_name="Отчество", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=50)
    birthday = models.DateField(verbose_name="Дата рождения")
    email = models.EmailField(verbose_name="e-mail")
    phone = PhoneField(verbose_name="Телефон")
    begin_work = models.DateField(verbose_name="Начало работы")
    end_work = models.DateField(verbose_name="Окончание работы", blank=True, null=True, help_text="Введите дату увольнения сотрудника")
    position = models.CharField(verbose_name="Должность", max_length=200)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Отдел")

    class Meta:
        db_table = "employee"
        ordering = ["last_name", "first_name", "middle_name"]

#    def get_absolute_url(self):
#        return reverse()

    def display_last_name(self):
        return '{0} {1} {2}'.format(self.last_name, self.first_name, self.middle_name)
    display_last_name.short_description = "Ф.И.О."

    def __str__(self):
        return self.display_last_name()
