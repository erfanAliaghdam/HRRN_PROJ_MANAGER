from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import ProcessSerializer
from processManager.models import Process

class ProcessViewSet(ModelViewSet):
    serializer_class = ProcessSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Process.objects.filter(user = self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        return super().perform_create(serializer)