from django.shortcuts import render
from django.views.generic import ListView
from employees.models import Employee

class EmployeeList(ListView):
    model = Employee

    def get_context_data(self, *, object_list=None, **kwargs):
