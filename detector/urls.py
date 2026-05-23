from django.urls import path
from . import views

urlpatterns = [

    # 🔥 HOME (after login)
    path('', views.home_view, name='home'),

    # AUTH
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # PAGES
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

    # ML PREDICTION
    path('predict/', views.predict_view, name='predict'),
]