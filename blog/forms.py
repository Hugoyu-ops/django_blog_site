from django import forms
from .models import Post, comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('text', )