from django.urls import path 
from .views import form_view, home
from book_review import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('form/', form_view, name='form_view'),
    path('home/', home, name='home'),
]

