from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from dogapi.controllers import BreedViewSet, DogViewSet


router = DefaultRouter()
router.register("dogs", DogViewSet)
router.register("breeds", BreedViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]