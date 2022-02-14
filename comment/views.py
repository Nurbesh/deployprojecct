from rest_framework.viewsets import ModelViewSet

from .models import Comment
from .serialaizers import CommentSerializer
from problem.views import PermissionMixin


class CommentViewSet(PermissionMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Create your views here.
