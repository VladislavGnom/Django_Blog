from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.show_posts, name='show'),
    path('blog/<int:post_id>', views.detail_post, name='detail'),
    path('blog/edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('blog/delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('blog/create_post', views.create_post, name='create_post'),
    path('blog/<username>/posts/', views.user_post_display, name='user_posts'),
]
