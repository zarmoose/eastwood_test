from django.test import TestCase
from django.urls import reverse
from employees import models
import datetime
import random


class IndexViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.number_of_departments = 5
        number_of_employees = 63

        cls.department_objs = []
        cls.employee_objs = []

        for department_num in range(cls.number_of_departments):
            d = models.Department.objects.create(name='Отдел {}'.format(department_num))
            cls.department_objs.append(d)

        for employee_num in range(number_of_employees):
            e = models.Employee.objects.create(
                first_name='Имя {}'.format(employee_num),
                middle_name='Отчество {}'.format(employee_num),
                last_name='Фамилия'.format(employee_num),
                birthday=datetime.date.today(),
                email='test@test.ru',
                phone='+76665554433',
                begin_work=datetime.date.today(),
                end_work=datetime.date.today(),
                position='Маркетолог',
                department=random.choice(cls.department_objs)
            )
            cls.employee_objs.append(e)

    def test_view_url_redirection(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 302)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/employees/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'employees/index.html')

    def test_pagination_is_15(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertTrue(len(resp.context['employees']) == 15)

    def test_lists_all_employees(self):
        resp = self.client.get(reverse('index') + '?page=5')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertTrue(len(resp.context['employees']) == 3)

    def test_url_page_is_0(self):
        resp = self.client.get(reverse('index') + '?page=0')
        self.assertEqual(resp.status_code, 404)

    def test_url_page_is_5(self):
        resp = self.client.get(reverse('index') + '?page=6')
        self.assertEqual(resp.status_code, 404)

    def test_url_working(self):
        resp = self.client.get(reverse('index') + '?working=on')
        self.assertEqual(resp.status_code, 200)

    def test_url_department_is_0(self):
        resp = self.client.get(reverse('index') + '?department=0')
        self.assertEqual(resp.status_code, 200)

    def test_url_department_is_greather_than_last(self):
        resp = self.client.get(reverse('index') + '?department={}'.format(self.number_of_departments + 1))
        self.assertEqual(resp.status_code, 200)


class EmployeeDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.department = models.Department.objects.create(name="Маркетинг")
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


    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/employees/{}/'.format(self.employee.id))
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('employee-detail', args=[str(self.employee.id)]))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('employee-detail', args=[str(self.employee.id)]))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'employees/employee_detail.html')

    def test_view_id_is_out_of_range(self):
        resp = self.client.get('/employees/{}/'.format(self.employee.id + 1))
        self.assertEqual(resp.status_code, 404)


class GlossaryViewTest(TestCase):
    fixtures = ['testdata.json']

    @classmethod
    def setUpTestData(cls):
        cls.departments = models.Department.objects.all()
        cls.employees = models.Employee.objects.all()

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/employees/glossary/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('glossary'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('glossary'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'employees/glossary.html')

    def test_pagination_is_15(self):
        resp = self.client.get(reverse('glossary'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertTrue(len(resp.context['employees']) == 15)

    def test_lists_all_employees(self):
        resp = self.client.get(reverse('glossary') + '?page=4')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'])
        self.assertTrue(len(resp.context['employees']) == 14)

    def test_url_page_is_0(self):
        resp = self.client.get(reverse('glossary') + '?page=0')
        self.assertEqual(resp.status_code, 404)

    def test_url_page_is_5(self):
        resp = self.client.get(reverse('glossary') + '?page=5')
        self.assertEqual(resp.status_code, 404)

    def test_url_group_is_0(self):
        resp = self.client.get(reverse('glossary') + '?group=0')
        self.assertEqual(resp.status_code, 200)

    def test_url_group_is_8(self):
        resp = self.client.get(reverse('glossary') + '?group=8')
        self.assertEqual(resp.status_code, 200)
