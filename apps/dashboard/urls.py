from django.urls import path


app_name='dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]