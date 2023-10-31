from django.urls import path
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView )
from .appViews.exampleView import ExampleView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("example",ExampleView.as_view(),name='example_view')
]