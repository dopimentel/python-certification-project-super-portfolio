from rest_framework import routers
from django.urls import path, include
from projects.views import (
    ProfileViewSet,
    ProjectViewSet,
    CertificateViewSet,
    CertifyingInstitutionViewSet,
)


router = routers.DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"certificates", CertificateViewSet, basename="certificate")
router.register(
    r"certifying-institutions",
    CertifyingInstitutionViewSet,
    basename="certifying_institution",
)


urlpatterns = [path("", include(router.urls))]
