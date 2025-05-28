#!/usr/bin/env python3
"""
Models for custom User, Conversation, and Message in messaging_app.
"""

import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    """Extends Django's default user model with future customization placeholders."""
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Conversation(models.Model):
    """Model to track users involved in a conversation."""
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='conversations'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id}"


class Message(models.Model):
    """Model to store messages in a conversation."""
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='messages_sent'
    )
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.id} from {self.sender.username}"
