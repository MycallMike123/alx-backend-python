# chats/permissions.py

from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allows access only to participants of a conversation.
    Assumes the view has a `.get_object()` method returning a Message or Conversation
    with sender and receiver or participants.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        # Check if user is part of the conversation/message
        return (
            hasattr(obj, "participants") and user in obj.participants.all()
        ) or (
            hasattr(obj, "sender") and obj.sender == user
        ) or (
            hasattr(obj, "receiver") and obj.receiver == user
        )
