from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('add_project/', views.add_project, name='add_project')
]