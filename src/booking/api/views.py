#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ViewSets for booking app models.

@author hielke
"""

from booking import models
from booking.api import serializers
from rest_framework import viewsets


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookingSerializer

    queryset = models.Booking.objects.all()
