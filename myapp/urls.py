from myapp import views
from django.urls import path
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.login_view,name='login'),
    path('register/', views.register_view,name='register'),
    path('projects', views.projects,name='projects'),
    path('contact', views.contact, name='contact'),
    path('list', views.list, name='list'),
    path('welcome', views.welcome, name='welcome'),
    
    
    path('', views.apiOverview, name="api-overview"),
	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),

	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]
