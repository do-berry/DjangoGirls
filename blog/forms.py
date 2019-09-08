from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # klucze z dict() tego co dodajemy
        fields = ('title', 'text',) # data ma być ustawiona automatycznie

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
