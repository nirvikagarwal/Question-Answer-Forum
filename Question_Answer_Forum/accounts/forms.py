import datetime
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import SelectDateWidget
from .models import User


class UserLoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self, *args, **kwargs):

        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:

            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("User Does Not Exist.")
            if not user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=SelectDateWidget(years=range(1960, 2019), attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ("first_name",
                  "last_name", 
                  "username", 
                  "email", 
                  "birth_date", 
                  "bio",  
                  "password1",
                  "password2",
                   )
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.TextInput(attrs={'class':'form-control'}),
        }
    

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birth_date = self.cleaned_data['birth_date']
        user.bio = self.cleaned_data['bio']
        if commit:
            user.save()
        return user
        