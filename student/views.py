from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from instructor.views import is_instructor
# Create your views here.
from course.models import Course

def is_student(user):
  return user.level == 200

@login_required
@user_passes_test(is_student)
def dashboard(request):
  # at this point, we are sure request.user is a valid object with user.level = 200
  return render(request, 'student/dashboard.html')

@login_required
@user_passes_test(is_student)
def availableCourses(request):
  courses = Course.objects.filter(registration_open=True)
  return render(request, 'student/availableCourses.html', {'courses': courses})

