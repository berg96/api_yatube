from django.urls import path, include

from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import PostViewSet

app_name = 'api'

router = SimpleRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
