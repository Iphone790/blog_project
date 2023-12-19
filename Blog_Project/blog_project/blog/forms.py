from django import forms
from blog.models import Comment
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class EmailSendForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    to = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),  # Adjust rows as needed
        }


class CustomSignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']




