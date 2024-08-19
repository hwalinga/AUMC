"""
Models for the booking system.
"""

import crum
from django.contrib.auth.models import User
from django.db import models


class Instrument(models.Model):
    """An instrument in the lab."""
    name = models.TextField()
    location = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_modified = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='instruments_created')
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name='instruments_modified')

    def save(self, *args, **kwargs):
        """Set the correct user for created_by and modified_by"""
        user = crum.get_current_user()
        if user and not user.pk:  # AnonymousUser
            user = None

        if not self.pk:
            self.created_by = self.created_by or user

        self.modified_by = user

        super().save(*args, **kwargs)


class Booking(models.Model):
    """A booking made for an instrument."""
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    instrument = models.ForeignKey(
        Instrument, on_delete=models.CASCADE, related_name='bookings')

    timestamp_start = models.DateTimeField()
    timestamp_end = models.DateTimeField()

    timestamp_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings_created')

    def save(self, *args, **kwargs):
        """Set the created_by"""
        if not self.created_by:
            self.created_by = crum.get_current_user()
        super().save(*args, **kwargs)
