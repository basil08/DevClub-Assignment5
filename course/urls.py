from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
  path('openRegistration/<int:course_id>', views.openRegistration, name='openRegistration'),
  path('closeRegistration/<int:course_id>', views.closeRegistration, name='closeRegistration'),
]