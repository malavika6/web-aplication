from django.core import validators
from django import forms
from . models import user

class admin(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'
        widgets={
            'username': forms.TimeInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True ,attrs={'class':'form-control'}),
        }
    

    
