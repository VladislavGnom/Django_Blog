from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

    
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

 
class CreatePostForm(EditPostForm):
    pass
