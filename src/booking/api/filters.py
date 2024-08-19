#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filters for the booking api.

@author hielke
"""

from booking import models
from django_filters import rest_framework as filters


class BookingFilter(filters.FilterSet):
    instrument = filters.NumberFilter(field_name='instrument__pk')
    user = filters.NumberFilter(field_name='created_by__pk')

    class Meta:
        model = models.Booking
        fields = []
