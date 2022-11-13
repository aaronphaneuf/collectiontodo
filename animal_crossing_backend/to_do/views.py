from django.shortcuts import render
from .models import User, Collection 
from .serializers import UserSerializer, CollectionSerializer, UserCollectionSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class UserCollectionViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCollectionSerializer

