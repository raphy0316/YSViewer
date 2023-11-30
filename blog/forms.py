from django import forms
from .models import Post, Comment, Document

class PostForm(forms.ModelForm): #게시물

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm): #댓글

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
