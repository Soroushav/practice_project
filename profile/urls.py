from django.urls import path
from .views import HomePageView, ProfilePageView, CreateUserView, EditUserView, SearchUserView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name='profile'),
    path('reg/signup/', CreateUserView.as_view(), name='signup'),
    path('profile/edit/<int:pk>/', EditUserView.as_view(), name='update'),
    path('profile/search/', SearchUserView.as_view(), name='search')
]