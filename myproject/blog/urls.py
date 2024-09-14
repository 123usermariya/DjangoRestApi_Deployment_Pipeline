# blog/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.post_list, name='post_list'),
# ]
# blog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
