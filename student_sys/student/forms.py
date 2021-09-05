from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    def clean_phone(self):
        cleaned_data = self.cleaned_data['phone']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('电话号码必须是数字')
        return int(cleaned_data)

    class Meta:
        model = Student
        fields = (
            'name', 'sex', 'profession',
            'email', 'phone','status'
        )

