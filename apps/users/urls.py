from django.urls import path

from apps.users.views import (UserListView)

urlpatterns = [
    path('list', UserListView.as_view(), name='users-list'),
]
