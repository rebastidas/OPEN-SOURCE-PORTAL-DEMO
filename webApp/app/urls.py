from django.urls import path
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView )
from .appViews.loginViews import loginView, logoutView
from .appViews.profileViews import profileView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("login/", loginView.LoginView.as_view(), name='login_view'),
    path("logout/", logoutView.LogoutView.as_view(), name='logout_view'),
    path("user-profile/<str:id>", profileView.ProfileView.as_view(), name='profile_view'),
    path("user-profile/", profileView.ProfileView.as_view(), name='create_profile_view')
]