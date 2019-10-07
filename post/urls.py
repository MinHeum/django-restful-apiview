from django.urls import path, include
from post import views

urlpatterns = [
    # 127.0.0.1:8000/post == ListView
    path('post/', views.PostList.as_view()),
    # 127.0.0.1:8000/post/<pk> == DetailView
    path('post/<int:pk>/', views.PostDetail.as_view()),
]
