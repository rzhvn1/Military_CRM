from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Document

class IsSuperUserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        docs_lst = ['public', 'private', 'secret', 'top-secret']
        group = request.user.groups.all()[0].name
        if request.method in SAFE_METHODS:
            return True
        elif group == 'general' and len(request.data) > 0:
            docs_lst.remove('top-secret')
            print(request.data)
            docs = str(request.data['document_root']) in docs_lst
            print(request.data['document_root'])
            print(docs)
            if docs == False:
                obj = Document.objects.get(title=request.data['title'])
                obj.delete()
                return True

        elif group == 'president':
                docs = request.data['document_root'] in docs_lst
                if docs:
                    return True
            # if group and docs:
            #     return True

        return request.user.groups.filter(name__in = ['general', 'president'])

class FilterObjPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            users_lst = ['general', 'president']
            docs_lst = ['public', 'private', 'secret', 'top-secret']
            group = request.user.groups.all()[0].name
            if group == 'general':
                docs_lst.remove('top-secret')
                docs = obj.document_root in docs_lst
            elif group == 'president':
                docs = obj.document_root in docs_lst
            if group and docs:
                return True




