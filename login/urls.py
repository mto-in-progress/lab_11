from django.urls import path
from login.views import LoginView

urlpatterns = [
    path('', LoginView.as_view())
]
