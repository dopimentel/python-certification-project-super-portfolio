from rest_framework import routers
from django.urls import path, include
from projects.views import ProfileViewSet


router = routers.DefaultRouter()
router.register(r"profiles", ProfileViewSet)

urlpatterns = [path("", include(router.urls))]