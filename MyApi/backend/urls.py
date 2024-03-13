from django.urls import path
from .views import ArticleList, ArticleDetails

urlpatterns = [
    path('api/articles/', ArticleList.as_view()),
    path('api/articles/<slug:slug>/', ArticleDetails.as_view())
]