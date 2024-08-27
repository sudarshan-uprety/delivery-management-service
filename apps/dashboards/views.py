from django.views.generic import TemplateView,ListView

from apps.users.mixins import AuthMixin


class DashboardView(AuthMixin, TemplateView):
    template_name = 'dashboards/dashboards.html'
    menu_active = 'dashboards'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
