from django.urls import path

from apps.users.views import (UserListView)

app_name='users'

urlpatterns = [
    path('list', UserListView.as_view(), name='users-list'),
]
