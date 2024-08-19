#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Permission utility classes.

@author hielke
"""


from django.http import Http404
from rest_framework import permissions


class IsOwnerOr404(permissions.BasePermission):
    """Give access if admin or if owner, otherwise 404.

    NB. The owner should be indicated with a field "created_by"
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superuser:
            return True  # Admin

        if obj.created_by_id == request.user.pk:
            return True  # Owner

        # Instead of return False, resulting in 403,
        # this returns a 404 which hides the existence of the instance.
        raise Http404
