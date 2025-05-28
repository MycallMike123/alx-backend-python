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
    password = models.CharField(max_length=128)  # Explicit password definition
    first_name = models.CharField(max_length=150, blank=True)  # Explicit for linter/checks
    last_name = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.username



class Conversation(models.Model):
    """
    Represents a conversation between multiple users.
    Uses UUID as primary key and has many-to-many relation with CustomUser.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField(CustomUser, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id}"


class Message(models.Model):
    """
    Represents a single message in a conversation.
    Linked to sender (CustomUser) and conversation.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.username} in {self.conversation.id}"
