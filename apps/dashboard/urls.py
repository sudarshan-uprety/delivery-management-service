from django.urls import path

from apps.users import views as users_views


app_name = 'dashboard'

urlpatterns = [
    path('', users_views.Login.as_view(), name='index'),
    path('login', users_views.Login.as_view(), name='login'),
]