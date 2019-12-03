"""Serializers for rental_app database models"""

from rest_framework import serializers

from . import models


class FriendSerializer(serializers.ModelSerializer):
    """Serializer for Friend model"""
    class Meta:
        """Fields for serializer"""
        model = models.Friend
        fields = ("id", "name")


class BelongingSerializer(serializers.ModelSerializer):
    """Serializer for Belonging model"""
    class Meta:
        """Fields for serializer"""
        model = models.Belonging
        fields = ("id", "name")


class BorrowedSerializer(serializers.ModelSerializer):
    """Serializer for Borrowed model"""
    class Meta:
        """Fields for serializer"""
        model = models.Borrowed
        fields = ("id", "what", "to_who", "when", "returned")
