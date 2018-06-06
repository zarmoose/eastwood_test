from django.conf.urls import url
from employees.views import EmployeeList

urlpatterns = [
    url('^$', EmployeeList.as_view())
]
