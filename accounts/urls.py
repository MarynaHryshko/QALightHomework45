from django.urls import path

from .views import home_view, login_view, RegisterView, logout_view


urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]

app_name = 'accounts'


