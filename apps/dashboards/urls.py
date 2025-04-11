from django.urls import path

from apps.users import views as users_views
from apps.dashboards import views as dashboard_views


app_name = 'dashboards'

urlpatterns = [
    path('', dashboard_views.DashboardView.as_view(), name='dashboard'),
    path('login', users_views.Login.as_view(), name='login'),
]