from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(max_length=25, help_text='Required.Password1 and Password2 must match', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=25, widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'age', 'email')

    def clean_password2(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise ValidationError("passwords did not match!")
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


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password',)

