from datetime import datetime

from django.db.models import Avg
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import (CurrentUserDefault, ModelSerializer,
                                        SerializerMethodField, ValidationError)

from reviews.models import Comment, Review
from titles.models import Category, Genre, Title


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id',)


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        exclude = ('id',)


class TitleSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    rating = SerializerMethodField()

    class Meta:
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category')
        read_only_fields = ('id', 'rating')
        model = Title

    def validate_year(self, year):
        if year > datetime.now().year:
            raise ValidationError(
                'Нельзя добавлять произведения из будущего.')
        return year

    def get_rating(self, obj):
        return obj.reviews.aggregate(average=Avg('score'))['average']


class ReviewSerializer(ModelSerializer):
    author = SlugRelatedField(
        slug_field='username', read_only=True, default=CurrentUserDefault())

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date',)
        read_only_fields = ('id', 'pub_date')

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data
        title_id = (self.context['request'].path).split('/')[4]
        author = self.context['request'].user
        if Review.objects.values(
            'author', 'title').filter(
                author=author, title__id=title_id).exists():
            raise ValidationError('Вы уже написали отзыв.')
        return data


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
        read_only_fields = ('id', 'author', 'pub_date')
