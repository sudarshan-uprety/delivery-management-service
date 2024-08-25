from django.urls import path

from apps.users import views as users_views
from apps.dashboard import views as dashboard_views


app_name = 'dashboard'

urlpatterns = [
    path('', dashboard_views.DashboardView.as_view(), name='index'),
    path('login', users_views.Login.as_view(), name='login'),
]