#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
URL router for Booking API.

@author hielke
"""

from booking.api import views
from django.urls import path

app_name = "booking"
urlpatterns = [
    path("bookings/<int:pk>/", views.BookingViewSet.as_view({'get': 'retrieve'})),
    path("bookings/", views.BookingViewSet.as_view({'get': 'list', 'post': 'create'})),
]
