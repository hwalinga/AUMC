#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ViewSets for booking app models.

@author hielke
"""

from booking import models
from booking.api import filters, serializers
from django.http import Http404
from main import permissions
from rest_framework import viewsets


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookingSerializer

    # Filtering
    lookup_field = "pk"  # default
    filterset_class = filters.BookingFilter

    # Permissions
    def get_queryset(self):
        """Perform permission check on the 'list' level."""
        objs = models.Booking.objects
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return objs.all()  # Admin

        if not user.pk:
            raise Http404  # AnonymousUser

        # When a user is not an admin, return the objects associated by them.
        return objs.filter(created_by=user)

    # Permission on the 'instance' level.
    permission_classes = [permissions.IsOwnerOr404]
