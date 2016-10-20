from django import forms

from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('title', 'student_first_name', 'student_first_name', 'student_email', 'text',)
