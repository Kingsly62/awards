from myapp import views
from django.urls import path
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.login_view,name='login'),
    path('register/', views.register_view,name='register'),
    path('projects', views.projects,name='projects'),
    path('contact', views.contact, name='contact'),
    path('list', views.list, name='list')
]
