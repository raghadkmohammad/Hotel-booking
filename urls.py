from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BookingViewSet, InvestmentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'investments', InvestmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
