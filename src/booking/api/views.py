#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ViewSets for booking app models.

@author hielke
"""

from booking import models
from booking.api import filters, serializers
from rest_framework import viewsets


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookingSerializer

    queryset = models.Booking.objects.all()

    # Filtering
    lookup_field = "pk"  # default
    filterset_class = filters.BookingFilter
