from django.shortcuts import render
from django.views import generic
from employees import models

class IndexView(generic.ListView):
    model = models.Employee
    context_object_name = 'employees'
#    queryset = models.Employee.objects.order_by('last_name', 'first_name', 'middle_name')
    template_name = 'employees/index.html'
    paginate_by = 20


class EmployeeDetail(generic.DetailView):
    model = models.Employee
    context_object_name = 'employee'
    template_name = 'employees/employee_detail.html'