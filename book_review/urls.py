from django.urls import path 
from .views import form_view, home, register_user, profile_view
from .api_views import RegisterApiview
from book_review import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    # path('register/', views.register_page, name='register'),
    path('api/register/',RegisterApiview.as_view(), name='api-register'),
    path('profile/', views.profile_view, name="profile"),
    path("book_info/", views.book_info, name="book-info"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('form/', form_view, name='form_view'),
    path('home/', home, name='home'),
]

