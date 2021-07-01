from django import forms
from .models import Comment, Profile, User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
            'user_name': 'Your Name',
            'user_email': 'Your Email',
            'text': 'Your Comment'
        }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('posts',)
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')