from .views import UserProfileView
from django.urls import path


urlpatterns = [
    path('profile/', UserProfileView.as_view()),
]