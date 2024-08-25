from django import forms
from django.contrib.auth import authenticate, login


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise forms.ValidationError("Email or password did not match.")
            if not user.is_active or not user.is_staff or not user.is_verified:
                raise forms.ValidationError('User is not active or you do not have permission.')
            cleaned_data['user'] = user
        return cleaned_data
