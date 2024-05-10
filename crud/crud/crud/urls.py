from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('signup/', views.SignupPage, name='signup'),
    path('', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
]
