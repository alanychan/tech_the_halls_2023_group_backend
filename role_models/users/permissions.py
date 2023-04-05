from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if ( request.method in permissions.SAFE_METHODS ) and permissions.IsAuthenticated  or permissions.IsAdminUser:
            return True
        return obj.id == request.user.id


class IsAdminOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if permissions.IsAdminUser:
            if  ( request.method in permissions.SAFE_METHODS ):
                return True
        return obj.id == request.user.id

