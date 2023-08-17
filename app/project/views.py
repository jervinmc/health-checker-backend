from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class ProjectView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Project.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=ProjectSerializer


