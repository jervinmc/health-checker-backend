from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Endpoint
from .serializers import EndpointSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from project.models import Project
from users.serializers import GetUserSerializer
from project.serializers import ProjectSerializer
import pusher
from decouple import config
class EndpointView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    queryset=Endpoint.objects.all()
    permissions_class = [permissions.AllowAny]
    serializer_class=EndpointSerializer

    def list(self,request):
        response = {
            "data": [],
            "status": status.HTTP_200_OK,
            "message": "SUCCESS",
            "status_code": "200",
        }
        try:
            project = request.query_params.get("project_id")
            instance = Endpoint.objects.filter(project = project)
            serializer_response = EndpointSerializer(instance, many=True)
            response['data'] = serializer_response.data

        except Exception as e:
            print(e)
            response["status"] = status.HTTP_500_INTERNAL_SERVER_ERROR
            response["message"] = "FAILED"
            response["status_code"] = "500"

        return Response(response)


