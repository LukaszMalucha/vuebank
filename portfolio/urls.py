from django.urls import path, include
from rest_framework.routers import DefaultRouter

from portfolio import views

router = DefaultRouter()
router.register('instruments', views.InstrumentViewSet)
router.register('cash-balance', views.CashBalanceViewSet)
router.register('asset-manager', views.AssetManagerViewSet, basename='asset-manager')
router.register('buy', views.BuyAssetViewSet)
router.register('sell', views.SellAssetViewSet, basename='sell')


app_name = 'portfolio'

urlpatterns = [
    path('', include(router.urls)),
    path("user/", views.CurrentUserApiView.as_view(), name="current-user")
]

