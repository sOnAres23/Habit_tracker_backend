from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = "Вы не являетесь создателем этой привычки!"

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        else:
            return False

    def has_permission(self, request, view):

        return request.method in SAFE_METHODS or request.user.is_authenticated
