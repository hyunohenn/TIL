from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/password/', views.change_password, name='change_password'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('withdraw/', views.withdraw, name='withdraw'),
    # path('force_logout/', views.force_logout, name='force_logout'),
]
