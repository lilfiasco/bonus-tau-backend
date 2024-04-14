from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse, Http404

from .models import Card
from .serializers import CardSerializer, CardCreateSerializer


class CardViewSet(viewsets.ModelViewSet):
    """View for listing cards of current user."""

    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        serializer = self.serializer_class
        if self.action == 'create':
            serializer = CardCreateSerializer

        return serializer

    def get_queryset(self):
        """Return queryset of cards belonging to current user."""
        user = self.request.user
        return Card.objects.filter(owner=user)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user != instance.owner:
            return Response(
                data={"error": "У вас нет прав редактировать объект."},
                status=status.HTTP_403_FORBIDDEN
            )

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    