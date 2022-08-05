from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from course.models import Course
from .forms import CreateNewCourseForm

def is_instructor(user):
  return user.level == 300

@login_required
@user_passes_test(is_instructor)
def dashboard(request):
  if request.method == 'GET':
    courses = Course.objects.filter(instructor=request.user.id, archived=False)
    archived_courses = Course.objects.filter(instructor=request.user.id, archived=True)
    return render(request, 'instructor/dashboard.html', { 'courses': courses, 'archived_courses': archived_courses})
  else:
    return HttpResponseBadRequest("Can only GET /dashboard")

@login_required
@user_passes_test(is_instructor)
def createNewCourse(request):
  if request.method == 'POST':
    form = CreateNewCourseForm(request.POST)
    if form.is_valid():
      form.save(instructor=request.user)
      messages.success(request, 'Course created successfully!')
      return render(request, 'instructor/newCourse.html')
    else:
      messages.error(request, "Bahut saare errors hai. Pehle theek karo phir try karna")
      # SUGGESTION:
      # return redirect('instructor:dashboard')
      return render(request, 'instructor/newCourse.html')
  else:
    form = CreateNewCourseForm()
  return render(request, 'instructor/newCourse.html', { 'form': form })

@login_required
@user_passes_test(is_instructor)
def getCourses(request):
  try:
    courses = Course.objects.filter(
      instructor=request.user.id,
      archived=False
    )
    return render(request, 'instructor/courses.html', {'courses': courses})
  except:
    raise
    # print("Error while fetching courses for instructor")
    # return HttpResponse('ERROR: check console')

@login_required
@user_passes_test(is_instructor)
def setArchive(request, course_id):
  try:
    course = Course.objects.get(pk=course_id)
    if course:
      course.archived = True
      course.save()
    else:
      messages.error(request, "Could not find course with id {}".format(course_id))
      return render(request, 'instructor/coursePage.html')
    return redirect('instructor:coursePage')
  except:
    # TODO: In prod, make this appropriate error message
    raise

@login_required
@user_passes_test(is_instructor)
def unsetArchive(request, course_id):
  try:
    course = Course.objects.get(pk=course_id)
    if course:
      course.archived = False
      course.save()
    else:
      messages.error(request, "Could not find course with id {}".format(course_id))
      return render(request, 'instructor/coursePage.html')
    return redirect('instructor:coursePage')
  except:
    # TODO: In prod, make this appropriate error message
    raise

@login_required
@user_passes_test(is_instructor)
def coursePage(request, course_id):
  print(request.path)
  print(request.get_full_path())
  course = Course.objects.get(pk=course_id)
  if not course:
    messages.error(request, "Could not find course with id {}".format(course_id))
    return render(request, 'instructor/coursePage.html')
  return render(request, 'instructor/coursePage.html', {'course': course})

