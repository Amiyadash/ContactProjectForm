from django.conf.urls import url
from django.urls import path
from LoginApp import views
urlpatterns=[
    url(r'^homepage/',views.home),
    url(r'^Register/',views.signup),
    #path('index/', views.home),
    path('signup/', views.signup),
    path('success/', views.success),
    path('existinguser/', views.loginform),
    path('verify/', views.login)

]