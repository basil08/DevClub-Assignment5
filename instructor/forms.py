from django import forms
from course.models import Course

class CreateNewCourseForm(forms.ModelForm):
  class Meta:
    model = Course
    fields = (
      'title',
      'code',
      'course_content',
      'comments',
      'synopsis',
      'slot',
      'year',
      'session'
    )

  def __init__(self, *args, **kwargs):
    super(CreateNewCourseForm, self).__init__(*args, **kwargs)
    for field in iter(self.fields):
      self.fields[field].widget.attrs.update({
        'class': 'form-control',
        'placeholder': None
      })
  #   instructor = kwargs.pop('instructor', None)
  #   if instructor:
  #     self.fields['instructor'] = instructor
  #   else:
  #     raise forms.ValidationError('INSTRUCTOR COULD NOT BE DETERMINED!')

  def save(self, commit=True, *args, **kwargs):
    course = super(CreateNewCourseForm, self).save(commit=False)
    instructor = kwargs.pop('instructor', None)
    if not instructor:
      raise forms.ValidationError('INSTRUCTOR COULD NOT BE DETERMINED')
    course.instructor = instructor
    if commit:
      course.save()
    return course
