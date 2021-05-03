from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.groups.filter(name__in = ['general', 'president'])

class FilterObjPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            group = request.user.groups.filter(name__in = ['general', 'president'])
            docs = obj.document_root in ['public', 'private', 'secret', 'top-secret']
            if group and docs:
                return True




