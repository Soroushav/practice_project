from django.urls import path
from .views import HomePageView, ProfilePageView, CreateUserView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name='profile'),
    path('reg/signup/', CreateUserView.as_view(), name='signup'),
]