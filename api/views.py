from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from api.filters import TitleFilter
from api.mixins import CategoryGenreMixinViewSet
from api.permissions import AdminOrReadOnly, AuthorStaffOrReadOnly
from api.serializers import (CategorySerializer, CommentSerializer,
                             GenreSerializer, ReviewSerializer,
                             TitleSerializer)
from reviews.models import Review
from titles.models import Category, Genre, Title


class TitleViewSet(ModelViewSet):
    """Модель обработки запросов к произведениям."""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (AdminOrReadOnly,)
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def perform_create(self, serializer):
        category_slug = self.request.data['category']
        category = get_object_or_404(Category, slug=category_slug)
        genre_slug = self.request.POST.getlist('genre')
        genres = Genre.objects.filter(slug__in=genre_slug)
        serializer.save(
            category=category,
            genre=genres,
        )

    def perform_update(self, serializer):
        category_slug = self.request.data['category']
        category = get_object_or_404(Category, slug=category_slug)
        genre_slug = self.request.POST.getlist('genre')
        genres = Genre.objects.filter(slug__in=genre_slug)
        serializer.save(
            category=category,
            genre=genres,
        )


class CategoryViewSet(CategoryGenreMixinViewSet):
    """Модель обработки запроса к категории произведения."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(CategoryGenreMixinViewSet):
    """Модель обработки запроса к жанру произведения."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (AuthorStaffOrReadOnly,)

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorStaffOrReadOnly,)

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        return review.comments.all()

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        serializer.save(author=self.request.user, review=review)
