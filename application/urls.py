from . import views
from django.urls import path


urlpatterns = [
    path('signup/', views.UserRegistrationView.as_view()),
    path('login/', views.UserLoginView.as_view()),
]