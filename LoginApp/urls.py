from django.conf.urls import url
from django.urls import path
from LoginApp import views
urlpatterns=[
    url(r'^login/',views.index),
    url(r'^Register/',views.signup),
    path('index/', views.home),
    path('login/signup/', views.signup),
    path('login/success/', views.success),
    path('login/loging/', views.loginform),
    path('login/verify/', views.login)
]