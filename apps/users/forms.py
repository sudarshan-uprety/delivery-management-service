from django import forms
from django.contrib.auth import authenticate, login


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ['email', 'password']

    def clean(self):
        if self.cleaned_data.get('email') and self.cleaned_data.get('password'):
            user = authenticate(username=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
            if user is None:
                raise forms.ValidationError("Email or password did not match.")
            if not user.is_active == 'Active' or not user.is_staff == True or not user.is_verified == True:
                raise forms.ValidationError('User is not active or you do not have permission.')
