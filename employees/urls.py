from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('glossary/', views.GlossaryView.as_view(), name='glossary'),
]
