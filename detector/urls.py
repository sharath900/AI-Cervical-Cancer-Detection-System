from django.urls import path
from . import views

urlpatterns = [

    # OPEN LOGIN FIRST
    path('', views.login_view, name='login'),

    # HOME PAGE
    path('home/', views.home_view, name='home'),

    path('about/', views.about_view, name='about'),

    path('contact/', views.contact_view, name='contact'),

    path('predict/', views.predict_view, name='predict'),

    path('register/', views.register_view, name='register'),

    path('logout/', views.logout_view, name='logout'),
]