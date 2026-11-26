from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.v1_routers import Defaultv1_router

from .views import CommentViewSet, GroupViewSet, PostViewSet

v1_router = Defaultv1_router()
v1_router.register('posts', PostViewSet)
v1_router.register('groups', GroupViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(v1_router.urls)),
]
