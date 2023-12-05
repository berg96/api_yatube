from rest_framework import viewsets

from posts.models import Group, Post
from rest_framework.generics import get_object_or_404

from .serializers import GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        print(self.request.data['group'])
        serializer.save(
            author=self.request.user,
            group=get_object_or_404(Group, id=int(self.request.data['group']))
        )


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
