from django import forms

from .models import BlogDb


class PostForm(forms.ModelForm):

    class Meta:
        model = BlogDb
        fields = ('title', 'text',)
