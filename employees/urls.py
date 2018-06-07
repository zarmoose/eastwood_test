from django.urls import path
from employees.views import EmployeeList

urlpatterns = [
    path('', EmployeeList.as_view(), name='index')
]