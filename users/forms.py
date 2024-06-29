from django import forms
from .models import Reviews
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['author', 'email', 'rating', 'comment']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

# class EditPassword(PasswordChangeForm):
#     new_password1 = forms.CharField(
#         label="New password",
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#     )
#     new_password2 = forms.CharField(
#         label="New password confirmation",
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#     )