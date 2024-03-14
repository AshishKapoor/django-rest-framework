from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    # sets the slug field as not required
    # and through signal pre_save it gets auto generated from title field
    slug = serializers.SlugField(read_only=True)
    # hides the field below from /api form
    author = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = '__all__'
