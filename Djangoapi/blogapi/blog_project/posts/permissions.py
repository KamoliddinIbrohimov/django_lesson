from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #only allowed to view
        if request.method in permissions.SAFE_METHODS:
            return True
        #permission to edit or write is granted only to the author of the post
        return obj.author == request.user