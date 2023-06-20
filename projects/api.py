from rest_framework import viewsets, permissions
from .models import Projects
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Projects.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = ProjectSerializer
