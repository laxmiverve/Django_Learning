from django import forms
from .models import Blog

class BlogForm(forms.Form):
    blog_title = forms.ModelChoiceField(queryset=Blog.objects.all(), label = "Select a blog")
