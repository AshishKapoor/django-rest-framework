from .models import Article
from .serializers import ArticleSerializer
from rest_framework import viewsets, mixins


class ArticleViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    lookup_field = 'slug'
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
