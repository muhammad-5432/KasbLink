from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from apps.filters import WorkerFilter
from apps.models import (
    Category, Service, Conversation, Message, Order, OrderImage,
    Review, ReviewImage, Favourite, User, WorkerProfile, Portfolio
)
from apps.serializers import (
    CategorySerializer, ServiceSerializer, ConversationSerializer, MessageSerializer,
    OrderSerializer, OrderImageSerializer, ReviewSerializer, ReviewImageSerializer,
    FavouriteSerializer, UserSerializer, WorkerProfileSerializer, PortfolioSerializer
)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WorkerProfileViewSet(ModelViewSet):
    queryset = WorkerProfile.objects.all()
    serializer_class = WorkerProfileSerializer

    filter_backends = DjangoFilterBackend, SearchFilter, OrderingFilter
    search_fields = 'services__title', 'bio', 'city'
    ordering_fields = 'rating',

    filterset_class = WorkerFilter,


class PortfolioViewSet(ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ConversationViewSet(ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderImageViewSet(ModelViewSet):
    queryset = OrderImage.objects.all()
    serializer_class = OrderImageSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewImageViewSet(ModelViewSet):
    queryset = ReviewImage.objects.all()
    serializer_class = ReviewImageSerializer


class FavouriteViewSet(ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
