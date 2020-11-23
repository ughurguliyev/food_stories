from django import forms

from .models import Category

class ContactForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField()


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=150)
    confirm_password = forms.CharField(max_length=150)


class LogInForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=200)


class ArticleCreationForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField()