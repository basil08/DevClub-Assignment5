from . import views
from django.urls import path

app_name = 'instructor'

urlpatterns = [
  path('dashboard/', views.dashboard, name='dashboard'),
  path('newCourse', views.createNewCourse, name='createNewCourse'),
  path('setArchive/<int:course_id>', views.setArchive, name='setArchive'),
  path('unsetArchive/<int:course_id>', views.unsetArchive, name='unsetArchive'),
  path('course/<int:course_id>', views.coursePage, name='coursePage')
]