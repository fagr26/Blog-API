# posts/urls.py
from django.urls import path
from .views import PostList, PostDetail , Users



urlpatterns = [
path('<int:pk>/', PostDetail.as_view()),
path('', PostList.as_view()),
path('users/',Users.as_view()),
]