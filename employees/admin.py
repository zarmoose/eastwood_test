from django.contrib import admin
from .models import Department, Employee

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('display_last_name', 'department', 'begin_work', 'end_work')
    list_filter = ('department',)