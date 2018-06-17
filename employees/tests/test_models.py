from django.test import TestCase
from employees import models
import datetime


class DepartmentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.department = models.Department.objects.create(name='Маркетинг')

    def test_name_label(self):
        field_label = self.department._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название отдела')

    def test_name_max_length(self):
        max_length = self.department._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_object_str(self):
        name = self.department.name
        self.assertEquals(name, str(self.department))


class EmployeeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.department = models.Department.objects.create(name='Маркетинг')
        cls.employee = models.Employee.objects.create(
            first_name='Иван',
            middle_name='Иванович',
            last_name='Иванов',
            birthday=datetime.date.today(),
            email='test@test.ru',
            phone='+76665554433',
            begin_work=datetime.date.today(),
            end_work=datetime.date.today(),
            position='Маркетолог',
            department=cls.department
        )

    def test_first_name_label(self):
        field_label = self.employee._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'Имя')

    def test_first_name_max_length(self):
        max_length = self.employee._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 50)

    def test_middle_name_label(self):
        field_label = self.employee._meta.get_field('middle_name').verbose_name
        self.assertEquals(field_label, 'Отчество')

    def test_middle_name_max_length(self):
        max_length = self.employee._meta.get_field('middle_name').max_length
        self.assertEquals(max_length, 50)

    def test_last_name_label(self):
        field_label = self.employee._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'Фамилия')

    def test_last_name_max_length(self):
        max_length = self.employee._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 50)

    def test_birthday_label(self):
        field_label = self.employee._meta.get_field('birthday').verbose_name
        self.assertEquals(field_label, 'Дата рождения')

    def test_email_label(self):
        field_label = self.employee._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'e-mail')

    def test_phone_label(self):
        field_label = self.employee._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'Телефон')

    def test_begin_work_label(self):
        field_label = self.employee._meta.get_field('begin_work').verbose_name
        self.assertEquals(field_label, 'Начало работы')

    def test_end_work_label(self):
        field_label = self.employee._meta.get_field('end_work').verbose_name
        self.assertEquals(field_label, 'Окончание работы')

    def test_end_work_blank(self):
        field_blank = self.employee._meta.get_field('end_work').blank
        self.assertTrue(field_blank)

    def test_end_work_help_text(self):
        field_help_text = self.employee._meta.get_field('end_work').help_text
        self.assertEquals(field_help_text, 'Введите дату увольнения сотрудника')

    def test_position_label(self):
        field_label = self.employee._meta.get_field('position').verbose_name
        self.assertEquals(field_label, 'Должность')

    def test_position_max_length(self):
        max_length = self.employee._meta.get_field('position').max_length
        self.assertEquals(max_length, 200)

    def test_get_absolute_url(self):
        self.assertEquals(self.employee.get_absolute_url(), '/employees/{}/'.format(self.employee.id))

    def test_object_str(self):
        fio = self.employee.display_last_name()
        self.assertEquals(fio, str(self.employee))
