from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .permissions import IsSuperUserOrReadOnly, FilterObjPermission
from .serializers import *
# Create your views here.

class DocumentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuperUserOrReadOnly, FilterObjPermission]
    serializer_class = DocumentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        try:
            group = self.request.user.groups.all()[0].name
        except IndexError:
            return Document.objects.filter(document_root__in=['public'])

        if group == 'general':
            docs = Document.objects.filter(document_root__in=['public', 'private', 'secret'])
        elif group == 'sergeant':
            docs = Document.objects.filter(document_root__in=['public', 'private'])
        elif group == 'user':
            docs = Document.objects.filter(document_root__in=['public'])
        else:
            docs = Document.objects.all()
        return docs
