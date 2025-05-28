#!/usr/bin/env python3
"""Models for user, conversation, and message functionality in messaging_app."""

from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Adds UUID as primary key, email, phone number, and explicit password field.
    """
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=128)_

