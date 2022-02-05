# django
from django.urls import path

# local
from . import views

app_name="users_app"

urlpatterns = [
    # template login
    path(
        'login/',
        views.LoginUser.as_view(),
        name='login'
    ),
    # Para Login y registro con Google
    path(
        'api/google-login/',
        views.GoogleLoginView.as_view(),
        name='users-google_login'
    ),
]