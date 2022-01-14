from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('myskills/', views.skills_index, name='index'),

    # django built-in path accounts/login for log in
    path('accounts/signup/', views.signup, name='signup'),
]