from django.urls import path
from .views import *

urlpatterns = [
    path('post/<int:pk>/delete/',DeletePost.as_view(),name = 'post_delete'),
    path('',HomePageView.as_view(),name='home'),
    path('post/<int:pk>',BlogDetailView.as_view(),name = 'post_detail'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('post/new/',NewPost.as_view(),name='post_new'),
    path('post/<int:pk>/edit',PostEdit.as_view(),name='post_edit'),
]