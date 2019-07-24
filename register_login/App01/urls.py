from django.urls import path
from App01.views import *


urlpatterns = [
    path('index/', index),
    path('register/',register),
    path('login/',login),
    path('logout/',logout),
    path('register_data/',register_data),
    path('howold/',howold),
    path('vc/',ViewsClass.as_view()),
    path('LoginUser/',LoginUserApi.as_view()),
    path('onlyHtml/',onlyHtml),
    path('vueHtml/',VueHtml),
]
