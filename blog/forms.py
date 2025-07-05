from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from blog.models import Article, Comment


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "username"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "re-password"
    }))

    class Meta:
        model = User
        fields = ["username","password1","password2"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "password"
    }))

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','info','photo','category']
        widgets = {
            'title': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title"
            }),
            'info': forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Information"
            }),
            'photo': forms.FileInput(attrs={
                "class": "form-control",
            }),
            'category': forms.Select(attrs={
                "class": "form-control",
            })
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('text',)
        widgets = {
            "text":forms.Textarea(attrs={
                "class":"form-control",
                "rows":3
            })
        }