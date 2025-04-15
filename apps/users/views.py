from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.shortcuts import render
from django.contrib.auth.models import Group

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

    # def dispatch(self, request, *args, **kwargs):
    #     perm = request.user.has_perm('users.view_user')
    #     if not perm:
    #         return render(request, '403.html', {'error_message': "You don't have permission to view users", 'sub_error_message':'Console to your admin.'}, status=403)            
    #     return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        page_number = self.request.GET.get('page', 1)
        items_per_page = 15
        context['page_index'] = (int(page_number)-1)*items_per_page
        context['names'] = User.objects.filter(is_archived=False)
        context['groups'] = Group.objects.all()
        return context 

    def get_queryset(self):
        name = self.request.GET.getlist('names')
        role = self.request.GET.getlist('roles')
        if name:
            return User.objects.filter(id__in=name, is_archived=False)
        if role:
            return User.objects.filter(groups__in=role, is_archived=False)
        user_list = User.objects.filter(is_staff=True, is_archived=False).order_by('-date_joined')
        return user_list   
