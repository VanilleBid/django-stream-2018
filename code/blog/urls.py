from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('post/<int:post_id>/', views.post_single, name='post-single')
]
