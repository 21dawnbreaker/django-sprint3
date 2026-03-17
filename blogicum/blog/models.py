from django.contrib.auth import get_user_model
from django.db import models

from core.models import PublishedModel

User = get_user_model()

CHAR_FIELD_MAX_LENGTH = 256


class Category(PublishedModel):
    title = models.CharField(
        max_length=CHAR_FIELD_MAX_LENGTH,
        verbose_name='Заголовок'
    )
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=(
            'Идентификатор страницы для URL; '
            'разрешены символы латиницы, цифры, '
            'дефис и подчёркивание.'
        )
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
        default_related_name = 'categories'


class Location(PublishedModel):
    name = models.CharField(
        max_length=CHAR_FIELD_MAX_LENGTH,
        verbose_name='Название места'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'
        default_related_name = 'locations'


class Post(PublishedModel):
    title = models.CharField(
        max_length=CHAR_FIELD_MAX_LENGTH,
        verbose_name='Заголовок'
    )
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=(
            'Если установить дату и время в будущем — '
            'можно делать отложенные публикации.'
        )
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        Location,
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date', 'id')
        default_related_name = 'posts'
