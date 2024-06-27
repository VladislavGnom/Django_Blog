from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.show_posts, name='show'),
    path('blog/<int:post_id>', views.detail_post, name='detail'),
]
