from blog import views
from django.urls import path,include

urlpatterns = [
    path('post/<str:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
     path('post/<str:pk>/', views.post_detail, name='post_detail'),
    path('', views.post_list, name='post_list')
]