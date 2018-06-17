from django.test import TestCase
from employees import forms, models


class FilterFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_departments = 2
        for department_num in range(number_of_departments):
            models.Department.objects.create(name='Отдел №{}'.format(department_num))
        cls.queryset = str(models.Department.objects.all())
        cls.form = forms.FilterForm()

    def test_department_label(self):
        field_label = self.form.fields['department'].label
        self.assertEqual(field_label, 'Выберите отдел')

    def test_department_queryset(self):
        queryset = str(self.form.fields['department'].queryset)
        self.assertEqual(queryset, self.queryset)

    def test_department_empty_label(self):
        self.assertEqual(self.form.fields['department'].empty_label, 'Все')

    def test_department_required(self):
        self.assertFalse(self.form.fields['department'].required)

    def test_working_label(self):
        label = self.form.fields['working'].label
        self.assertEqual(label, 'Только работающие')

    def test_working_required(self):
        self.assertFalse(self.form.fields['working'].required)
