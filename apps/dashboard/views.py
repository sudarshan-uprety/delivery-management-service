from django.views.generic import TemplateView,ListView

from apps.users.mixins import AuthMixin


class DashboardView(AuthMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'
    menu_active = 'dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
