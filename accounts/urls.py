from django.urls import path

from .views import home_view, login_view, RegisterView, logout_view, ActivateAccountView



urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path(
        "activate/<str:username>/<str:token>/",
        ActivateAccountView.as_view(),
        name="activate",
    ),
]

app_name = 'accounts'


