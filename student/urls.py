from django.urls import path

app_name = 'student'
from . import views

urlpatterns = [
  path('dashboard/', views.dashboard, name='dashboard'),
  path('availableCourses', views.availableCourses, name='availableCourses')
]