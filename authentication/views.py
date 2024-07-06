from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView

from authentication.models import User
from authentication.serializers import UserCreateSerializer, UserListSerializer


class UserCreateView(CreateAPIView):
    """Класс создания пользователя"""
    model = User
    serializer_class = UserCreateSerializer

class UserListView(ListAPIView):
    """Класс получения списка пользователей"""
    model = User
    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.all()


