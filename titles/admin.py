from django.contrib.admin import ModelAdmin, register

from api_yamdb.settings import EMPTY_STRING_FOR_ADMIN_PY
from .models import Category, Genre, Title

ModelAdmin.empty_value_display = EMPTY_STRING_FOR_ADMIN_PY


@register(Title)
class TitleAdmin(ModelAdmin):
    list_display = (
        'pk', 'category', 'name', 'year', 'description', 'get_genres')
    search_fields = ('name',)
    list_filter = ('name',)

    def get_genres(self, obj):
        return '\n'.join([str(genre) for genre in obj.genre.all()])


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    search_fields = ('name',)
    list_filter = ('slug',)
    prepopulated_fields = {'slug': ('name',)}


@register(Genre)
class GenreAdmin(ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    search_fields = ('name',)
    list_filter = ('slug',)
    prepopulated_fields = {'slug': ('name',)}
