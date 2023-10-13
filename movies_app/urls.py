# movies_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'likes', views.LikeViewSet)
router.register(r'matches', views.MatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
