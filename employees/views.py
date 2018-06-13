from django.views import generic
from employees import models, forms, glossary
from django.core.paginator import InvalidPage

class IndexView(generic.ListView):
    context_object_name = 'employees'
    template_name = 'employees/index.html'
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        init = {}
        context = super(IndexView, self).get_context_data(**kwargs)
        department = self.request.GET.get('department')
        working = self.request.GET.get('working')
        if department:
            init['department'] = department
        if working:
            init['working'] = True
        filter_form = forms.FilterForm(initial=init)
        context['filter_form'] = filter_form
        return context

    def get_queryset(self):
        queryset = models.Employee.objects.all()
        department = self.request.GET.get('department')
        working = self.request.GET.get('working')
        if department:
            queryset = queryset.filter(department=department)
        if working:
            queryset = queryset.filter(end_work__isnull=True)
        return queryset


class EmployeeDetail(generic.DetailView):
    model = models.Employee
    context_object_name = 'employee'
    template_name = 'employees/employee_detail.html'


class GlossaryView(generic.ListView):
    model = models.Employee
    context_object_name = 'employees'
    template_name = 'employees/glossary.html'
    paginate_by = 15

    def __init__(self):
        super(GlossaryView, self).__init__()
        self.gloss = glossary.AlphabetGlossary(models.Employee.objects.all())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GlossaryView, self).get_context_data(**kwargs)
        context['group'] = self.gloss.group(1)
        return context
