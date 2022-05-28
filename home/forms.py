from django import forms
from .models import Bmi
from django.contrib.auth.forms import AuthenticationForm

class Bmform(forms.ModelForm):
    class Meta:
        model=Bmi
        fields = ['weight','hight','age']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class']='form-control'

class Login(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class']='form-control'