"""Api views for rental_app"""

from rest_framework import viewsets

from . import models, serializers


class FriendViewset(viewsets.ModelViewSet):
    """View for Friend"""
    queryset = models.Friend.objects.all()
    serializer_class = serializers.FriendSerializer


class BelongingViewset(viewsets.ModelViewSet):
    """View for Belonging"""
    queryset = models.Belonging.objects.all()
    serializer_class = serializers.BelongingSerializer


class BorrowedViewset(viewsets.ModelViewSet):
    """View for Borrowed"""
    queryset = models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer
