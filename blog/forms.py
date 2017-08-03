from django import forms
from .models import Post, Comment, Message
# our new form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('email', 'name', 'subject', 'message')
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
