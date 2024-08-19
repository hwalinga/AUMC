#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Serializers for booking app.

@author hielke
"""

from booking import models
from rest_framework import serializers


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'
