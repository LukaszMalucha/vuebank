from django.urls import path, include
from rest_framework.routers import DefaultRouter

from portfolio import views

router = DefaultRouter()
router.register('instruments', views.InstrumentViewSet)
router.register('asset-manager', views.AssetManagerViewSet, basename='asset-manager')


app_name = 'portfolio'

urlpatterns = [
    path('', include(router.urls)),
]

