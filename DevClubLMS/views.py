from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
  if request.user.level == 100:
    return redirect('admin:dashboard')
  elif request.user.level == 200:
    return redirect('student:dashboard')
  elif request.user.level == 300:
    return redirect('instructor:dashboard')
  else:
    return Http404("UNKNOWN USER! SOMETHING WENT WRONG!")