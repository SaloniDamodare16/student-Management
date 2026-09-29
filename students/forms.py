from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'email', 'age']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter student name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter email address'
            }),

            'age': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter age',
                'min': '1'
            }),
        }