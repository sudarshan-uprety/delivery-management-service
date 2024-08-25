from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from apps.users import mixins, forms


def dashboard(request):
    return render(request, 'account/login.html')


class Login(mixins.LoginMixin):
    template_name = 'account/login.html'
    form_class = forms.LoginForm

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
