from django.urls import path
from . import views

app_name = 'workshop'
urlpatterns = [
    path('login/', views.loginf, name='login'),
    path('register/', views.registerf, name='register'),
    path('', views.indexf, name='index'),
    path('newcut/', views.newcutf, name='newcut'),
    path('salary/', views.salaryf, name='salary'),
    path('newjob/', views.newjobf, name='newjob'),
    path('logout/', views.logoutf, name='logout'),
    path('api/newjob_sizes/<int:selected_cut>/', views.newjob_sizes, name='newjob_sizes'),
    path('api/newjob_colors/<int:selected_size>/', views.newjob_colors, name='newjob_colors'),
    path('api/newjob_lines/<int:selected_color>/', views.newjob_lines, name='newjob_lines'),
]