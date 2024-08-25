from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout


class AuthMixin(LoginRequiredMixin):
    login_url = reverse_lazy('dashboard:login')


class GuestMixin:
    redirect_url = reverse_lazy('dashboard:index')
    login_url = reverse_lazy('dashboard:index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect(self.redirect_url)


class LoginMixin(GuestMixin, FormView):

    def get_redirect_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        return self.login_url

    def get_login_url(self):
        if self.request.GET.get('next'):
            return self.login_url + '?next=' + self.request.GET.get('next')
        return self.login_url

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect(self.get_redirect_url())

        return redirect(self.get_login_url())


class GroupRequiredMixin:
    group_required = []

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PermissionRequiredMixin:
    permission_required = None

    def dispatch(self, request, *args, **kwargs):
        if not self.permission_required:
            raise ValueError("PermissionRequiredMixin requires 'permission_required' attribute to be set.")

        if not request.user.has_perm(self.permission_required):
            return render(request, '403.html', {
                'error_message': "You don't have permission to access this page",
                'sub_error_message': 'Contact your admin for assistance.'
            }, status=403)

        return super().dispatch(request, *args, **kwargs)
