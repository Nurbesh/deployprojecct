from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import ProblemSerializer, ReplySerializer
from .permissions import IsAuthorPermission
from .models import Problem, Reply
from account.permissions import IsActive


class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsActive]
        if self.action in ['update', 'partial_update', 'destroi']:
            permissions = [IsAuthorPermisson]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permission]


class ProblemViewSet(PermissionMixin, ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    
    def get_serializer_class(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context


class ReplyViewSet(PermissionMixin, ModelViewSet):
        queryset = Reply.objects.all()
        serializer_class = ReplySerializer