from django.contrib import admin
from django.urls import path

from demopage import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
        path('Login/', views.login,name='Login'),
        path('register/', views.register,name='register'),
        path('profile/',views.profile,name='profile'),
          path('contact/', views.contact, name='contact'),
        path('About/', views.about_view, name='About'),
       path('services/', views.Services, name='Services'),

            

]

