from django.urls import path
from .views import article_list, article_details

urlpatterns = [
    path('api/articles/', article_list),
    path('api/articles/<slug:slug>/', article_details)
]