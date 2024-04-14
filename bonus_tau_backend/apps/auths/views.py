import logging
from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .serializers import MyTokenObtainPairSerializer, UserRegisterSerializer, UserMeSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    """LoginView."""

    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserRegisterView(generics.CreateAPIView):
    """Register New User."""

    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer


class UserMeViewSet(
    viewsets.GenericViewSet
):
    queryset = CustomUser.objects.all()
    serializer_class = UserMeSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET'], detail=False, url_path='me')
    def me(self, requests, *args, **kwargs) -> Response:
        if self.request.user.is_authenticated:
            try:
                user = self.request.user
                serializer = self.get_serializer(user)
                return Response(serializer.data)
            except Exception as e:
                logging.exception('Error user me: %s', str(e))
                return Response({'error': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_404_NOT_FOUND)
    