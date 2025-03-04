from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class': 'form-control bg-dark text-light border-secondary','placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control bg-dark text-light border-secondary','placeholder': 'Your email'}))
    to = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control bg-dark text-light border-secondary','placeholder': 'Recipient\'s email'}))
    comments = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': 'form-control bg-dark text-light border-secondary','rows': 4,'placeholder': 'Your comments (optional)'}))

class CommentForm(forms.ModelForm):
 class Meta:
    model = Comment
    fields = ['name', 'email', 'body']