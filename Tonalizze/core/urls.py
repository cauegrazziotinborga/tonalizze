from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('config/', views.config_tonalidades_view, name='config_tonalidades'),
    path('info/', views.user_info_view, name='user_info'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
]
