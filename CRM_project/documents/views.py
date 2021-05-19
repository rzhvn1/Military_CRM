from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from .permissions import IsSuperUserOrReadOnly
from .serializers import *
# Create your views here.

class DocumentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuperUserOrReadOnly]
    serializer_class = DocumentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']


    @action(detail=True, methods=['get'])
    def get_queryset(self):
        try:
            group = self.request.user.groups.all()[0].name
        except IndexError:
            return Document.objects.filter(document_root__in=['public'], status='active')

        if group == 'general':
            docs = Document.objects.filter(document_root__in=['public', 'private', 'secret'], status='active')
        elif group == 'sergeant':
            docs = Document.objects.filter(document_root__in=['public', 'private'], status='active')
        elif group == 'user':
            docs = Document.objects.filter(document_root__in=['public'], status='active')
        else:
            docs = Document.objects.all()
        return docs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




