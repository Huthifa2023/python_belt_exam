from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),   #default route to main page, only if there is a logged in user(if not redirect to login page)


    path('login', views.login),     #render login and registration page


    path('add_user', views.add_user),   #POST request to add new user


    path('login_request', views.login_request),   #POST request to login , success will redirect to main page


    path('logout', views.logout),   #logout anchor request, clear the session redirct to login page

    
]