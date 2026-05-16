from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.views import (
    CategoryViewSet, ServiceViewSet, ConversationViewSet, MessageViewSet,
    OrderViewSet, OrderImageViewSet, ReviewViewSet, ReviewImageViewSet,
    FavouriteViewSet, UserViewSet, WorkerProfileViewSet, PortfolioViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'worker-profiles', WorkerProfileViewSet)
router.register(r'portfolios', PortfolioViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-images', OrderImageViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'review-images', ReviewImageViewSet)
router.register(r'favourites', FavouriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]