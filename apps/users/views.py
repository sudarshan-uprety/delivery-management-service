from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from apps.users.mixins import LoginMixin, AuthMixin, PermissionRequiredMixin
from apps.users import forms

User = get_user_model()


class Login(LoginMixin):
    template_name = 'account/login.html'
    form_class = forms.LoginForm

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserListView(AuthMixin, PermissionRequiredMixin, ListView):
    permission_required = 'users.view_user'
    paginate_by = 15
    template_name = 'users/list.html'
    model = User
    context_object_name = 'users'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        page_number = self.request.GET.get('page', 1)
        items_per_page = 15
        context['page_index'] = (int(page_number)-1)*items_per_page
        context['names'] = User.all_objects.all()
        return context

    def get_queryset(self):
        name = self.request.GET.get('name')
        role = self.request.GET.get('role')
        queryset = User.all_objects.all()
        if name:
            queryset = queryset.filter(name__icontains=name)
        if role:
            queryset = queryset.filter(role__icontains=role)
        return queryset

