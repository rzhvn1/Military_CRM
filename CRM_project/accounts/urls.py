from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('dossier', DossierModelViewSet, basename='dossier')
router.register('register', RegisterViewSet, basename="register")

urlpatterns = [
    path('', include(router.urls)),
    path('login/', AuthView.as_view(), name="authorization"),
    path('dossier/', DossierModelViewSet.as_view(), name = 'dossier')
]