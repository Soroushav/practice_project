from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .email import create_user_sent_email


class CustomUserCreationForm(forms.ModelForm):
    # password = forms.CharField(max_length=25)
    password2 = forms.CharField(max_length=25)

    class Meta:
        model = get_user_model()
        fields = ('username', 'age', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': "Your Password Baby"})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': "Your Password Again Baby"})
        self.fields['username'].help_text = "*"
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': "Your Username"})
        self.fields['password'].help_text = "*.Password1 and Password2 must match"

    def clean_password2(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError("passwords did not match!", code="invalid")
        return self.cleaned_data['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


# class CustomUserCreationForm(Form):
#     class Meta:
#         model = get_user_model()
#         fields = ('username','age')

class CustomUserChangeForm(forms.ModelForm):
    username = forms.CharField(max_length=25, help_text="*",
                               widget=forms.TextInput(attrs={"placeholder": "Your Username"}))
    password = forms.CharField(max_length=25, help_text='*.Password1 and Password2 must match',
                               widget=forms.PasswordInput(attrs={"placeholder": "Your Password"}))
    password2 = forms.CharField(max_length=25,
                                widget=forms.PasswordInput(attrs={"placeholder": "Your Password again."}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'age', 'email', 'password', 'password2')

# class CustomUserChangeForm(UserChangeForm):
#     # class Meta:
#     #     model = get_user_model()
#     #     fields = ('username', 'password',)

