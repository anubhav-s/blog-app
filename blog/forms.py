from django import forms

from .models import BlogDb


class PostForm(forms.ModelForm):
    """
    Using Django forms to create text boxes namely title and text.
    """
    class Meta:
        model = BlogDb
        fields = ('title', 'text',)
