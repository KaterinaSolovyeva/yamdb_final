from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, TextField


class MyUser(AbstractUser):
    """Модель юзера с выбором роли."""
    USER = 'user'
    MODERATOR = 'moderator'
    ANONYMOUS = 'anonymous'
    ADMIN = 'admin'
    ROLES = [
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
        (ANONYMOUS, 'Аноним'),
    ]

    username = CharField(
        verbose_name='Никнейм',
        max_length=150,
        unique=True
    )
    email = EmailField(
        max_length=150,
        unique=True,
        verbose_name='Почта'
    )
    first_name = CharField(
        max_length=30,
        blank=True,
        verbose_name='Имя'
    )
    last_name = CharField(
        max_length=30,
        blank=True,
        verbose_name='Фамилия'
    )
    bio = TextField(
        blank=True,
        null=True,
        verbose_name='О себе'
    )
    role = CharField(
        max_length=30,
        choices=ROLES,
        default=USER,
        verbose_name='Роль'
    )
    confirmation_code = CharField(
        max_length=70,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Проверочный код'
    )

    @property
    def is_admin(self):
        return self.is_superuser or self.role == MyUser.ADMIN

    @property
    def is_moderator(self):
        return self.role == MyUser.MODERATOR

    @property
    def is_user(self):
        return self.role == MyUser.USER

    class Meta:
        """Дополнительная информация по управлению моделью MyUser."""
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
