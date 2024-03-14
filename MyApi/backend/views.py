from .models import Article
from .serializers import ArticleSerializer
from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor


class ArticleViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # authentication_classes = (TokenAuthentication)
    permission_classes = [IsAuthenticated, IsAuthor]

    # Sets default auther value as session user
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)