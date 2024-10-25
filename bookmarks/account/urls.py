from django.urls import path
from account import views
from bookmarks.urls import urlpatterns



urlpatterns = [
    path('login/', views=views.login_views, name='login')
]