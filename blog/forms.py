from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Post, Category

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-3 py-2 border border-gray-300 bg-white rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': f'Enter {field.label}'
            })

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class StyledLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = (
                'w-full px-3 py-2 border border-gray-300 rounded bg-white '
                'focus:outline-none focus:ring-2 focus:ring-blue-500'
            )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border border-gray-300 bg-white rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Enter post title'
        })
        self.fields['content'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border border-gray-300 bg-white rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Write your content here...'
        })
        self.fields['categories'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border border-gray-300 bg-white rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
        })


