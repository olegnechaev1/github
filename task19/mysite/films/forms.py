from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Film

User = get_user_model()


class Filmsform(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('comment',)
        

class AuthUserform(AuthenticationForm, forms.ModelForm):
    class Meta:
       model = User 
       fields = ('password',)
       

class RegistrUserform(forms.ModelForm):
    class Meta:
        model = User
        help_texts = {'username': None}
        fields = ('username', 'password', 'email')
        
    def save(self, commit=True):
        user = super(RegistrUserform, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
