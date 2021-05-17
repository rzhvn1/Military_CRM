from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Document

class IsSuperUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.groups.filter(name__in = ['general', 'president'])




