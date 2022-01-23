from django.urls import path

from api.views.auth_views import *


app_name = 'auth'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]