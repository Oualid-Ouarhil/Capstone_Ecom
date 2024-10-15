from django.urls import path
from . import views
from .views import permission_classes, register


urlpatterns = [
    path('register/', views.register,name='register'),
    path('profile/', views.online_user,name='user_info'),
]