from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from instructor.views import is_instructor
from django.contrib import messages

from course.models import Course

@login_required
@user_passes_test(is_instructor)
def openRegistration(request, course_id):
  print("DEBUG: username", request.user.username)
  course = Course.objects.get(pk=course_id)
  course.registration_open = True
  course.save()
  return redirect('instructor:coursePage', course_id=course_id)

@login_required
@user_passes_test(is_instructor)
def closeRegistration(request, course_id):
  course = Course.objects.get(pk=course_id)
  course.registration_open = False
  course.save()
  return redirect('instructor:coursePage', course_id=course_id)


# @login_required
# @user_passes_test(is_instructor)
# def setArchive(request, course_id):
#   try:
#     course = Course.objects.get(pk=course_id)
#     if course:
#       course.archived = True
#       course.save()
#     else:
#       messages.error(request, "Could not find course with id {}".format(course_id))
#       return render(request, 'instructor/dashboard.html')
#     return redirect('instructor:dashboard')
#   except:
#     # TODO: In prod, make this appropriate error message
#     raise

# @login_required
# @user_passes_test(is_instructor)
# def unsetArchive(request, course_id):
#   try:
#     course = Course.objects.get(pk=course_id)
#     if course:
#       course.archived = False
#       course.save()
#     else:
#       messages.error(request, "Could not find course with id {}".format(course_id))
#       return render(request, 'instructor/dashboard.html')
#     return redirect('instructor:dashboard')
#   except:
#     # TODO: In prod, make this appropriate error message
#     raise