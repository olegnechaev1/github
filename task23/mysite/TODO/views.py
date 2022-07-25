from django.utils import timezone
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = ['status']
    
    def get_queryset(self):
        current_date = timezone.now()
        return Task.objects.filter(
            user=self.request.user, created__gte=current_date)
