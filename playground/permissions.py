from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Read-only requests are allowed for everyone.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Write permissions only allowed to the owner
        return obj.owner == request.user
