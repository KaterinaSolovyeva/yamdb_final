from django.contrib.admin import ModelAdmin, register

from api_yamdb.settings import EMPTY_STRING_FOR_ADMIN_PY

from .models import MyUser

ModelAdmin.empty_value_display = EMPTY_STRING_FOR_ADMIN_PY


@register(MyUser)
class MyUserAdmin(ModelAdmin):
    list_display = (
        'id', 'username', 'email', 'role', 'bio',
        'first_name', 'last_name', 'confirmation_code')
    list_editable = ('role',)
    search_fields = ('username', 'email')
