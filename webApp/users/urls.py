from django.urls import path
from .views import userApiView

urlpatterns =[
    path("registration/", userApiView.RegistrationView.as_view(), name='registration_view' )
]