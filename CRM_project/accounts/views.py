from django.shortcuts import render
from rest_framework import views, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .models import *
from .serializers import DossierSerializer, RegisterSerializer, CarSerializer, EducationSerializer, WarcraftSerializer
from rest_framework import viewsets
from .serializers import RegisterSerializer
# Create your views here.

class DossierModelViewSet(views.APIView):
    # serializer_class = DossierSerializer
    #
    # def get_queryset(self):
    #     dossier = Dossier.objects.get(user=self.request.user)
    #     return dossier

    def get(self, request, *args, **kwargs):
        try:
            dossier = Dossier.objects.get(user=request.user)
        except Dossier.DoesNotExist:
            return Response({"data":"Dossier doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = RegisterSerializer(dossier)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        dossier = Dossier.objects.get(user=request.user)
        serializer = RegisterSerializer(dossier, data=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response("Successfully updated!")
        return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        dossier = Dossier.objects.get(user=request.user)
        dossier.delete()
        return Response({"data":"OK!"})





class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class AuthView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key})