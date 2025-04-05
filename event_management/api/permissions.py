from rest_framework import permissions

class IsOrganizerOrReadOnly(permissions.BasePermission):
    """
    Only allow the event organizer to edit or delete the event.
    """

    def has_object_permission(self, request, view, obj):
        # Safe methods = GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the organizer
        return obj.organizer == request.user
