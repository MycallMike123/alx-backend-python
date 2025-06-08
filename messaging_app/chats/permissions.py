from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission to ensure users only access their own messages/conversations.
    """

    def has_object_permission(self, request, view, obj):
        return (
            getattr(obj, 'user', None) == request.user or
            getattr(obj, 'sender', None) == request.user or
            getattr(obj, 'receiver', None) == request.user
        )
