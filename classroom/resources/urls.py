from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.get_resources, name='get_resources'),
    path('schedule/', views.add_schedule, name='add_schedule'),
    path('maintenance/', views.add_maintenance, name='add_maintenance'),
]