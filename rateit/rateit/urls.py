from django.contrib import admin
from django.urls import path
from members.views import *
from members.views import check_username_availability


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('login/', sign_in, name="signin"),
    path("login/loggingin", loggingin, name="loggingin"),
    path('signup/', sign_up, name='signup'),
    path('signup/register/', register, name='register'),
    path('check-username-availability/', check_username_availability, name='check_username_availability'),  # Add this line
]
