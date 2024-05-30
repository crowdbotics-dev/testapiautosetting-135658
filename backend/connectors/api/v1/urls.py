from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135658ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135658", Testconnectors135658ViewSet, basename="testconnectors135658"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
