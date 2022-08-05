from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

from authentication.models import User

COURSE_SESSION_CHOICES = (
  ('Spring', 'Spring'),
  ('Fall', 'Fall'),
  ('Summer', 'Summer')
)

def is_valid_code(code):
  codes = Course.objects.filter(code=code)
  if len(codes) != 0:
    raise ValidationError("Duplicate course code! Please use another code")

def validate_year(year):
  # validators raise ValidationError if condition is not met
  if year < date.today().year:
    raise ValidationError("Course year cannot be less than current year!")

class Course(models.Model):
  title = models.CharField(max_length=200)
  code = models.CharField(max_length=6, validators=[is_valid_code])
  synopsis = models.CharField(max_length=120, null=True, blank=True)
  course_content = models.TextField()
  comments = models.CharField(max_length=200, blank=True, null=True)
  slot = models.CharField(max_length=2)
  year = models.IntegerField(validators=[validate_year])
  session = models.CharField(max_length=12, choices=COURSE_SESSION_CHOICES)
  archived = models.BooleanField(default=False)
  registration_open = models.BooleanField(default=True)
  instructor = models.ForeignKey(
    User,
    limit_choices_to={'level': 300}, # only instructor can create courses
    on_delete=models.CASCADE)
  students = models.ManyToManyField(User, limit_choices_to={ 'level': 200}, related_name='courses')
