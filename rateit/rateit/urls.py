from django.contrib import admin
from django.urls import path
from members.views import *
from profiles.views import *
<<<<<<< HEAD

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('login/',sign_in,name="signin"),
    path('signup/',sign_up,name='signup'),
    path('signup/register/', register_user, name='register'),
    path('signup/success/', registration_success, name='registration_success'),
    path('profiles', profiles, name='profiles')
=======
from members.views import check_username_availability


urlpatterns = [
    path('admin/', admin.site.urls),
    # memebers url
    path('', home, name="home"),
    path('login/', sign_in, name="signin"),
    path("login/loggingin", loggingin, name="loggingin"),
    path('signup/', sign_up, name='signup'),
    path('signup/register/', register, name='register'),
    path('check-username-availability/', check_username_availability, name='check_username_availability'),
    path('logout',logout_view,name="logout"),

    # profiles url
    path('land/',land,name="landingpag"),
>>>>>>> landingpage
]
