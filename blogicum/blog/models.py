from django.db import models

from core.models import PublishedModel, CreatedAtModel

from django.contrib.auth import get_user_model

User = get_user_model()


class Category(PublishedModel, CreatedAtModel):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(
        max_length=256, blank=False, verbose_name=("Заголовок"))
    description = models.TextField(blank=False, verbose_name=("Описание"))
    slug = models.SlugField(
        unique=True,
        blank=False,
        verbose_name="Идентификатор",
        help_text=("Идентификатор страницы для URL; "
                   "разрешены символы латиницы, цифры, дефис и подчёркивание.")
    )
    is_published = models.BooleanField(
        default=True,
        blank=False,
        verbose_name=("Опубликовано"),
        help_text="Снимите галочку, чтобы скрыть публикацию."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, verbose_name=("Добавлено"))

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class Location(PublishedModel, CreatedAtModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(
        max_length=256, blank=False, verbose_name=("Название места"))
    is_published = models.BooleanField(
        default=True, blank=False, verbose_name=("Опубликовано"))
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, verbose_name=("Добавлено"))

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.title


class Post(PublishedModel, CreatedAtModel):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(
        max_length=256, blank=False, verbose_name=("Заголовок"))
    text = models.TextField(blank=False, verbose_name=("Текст"))
    pub_date = models.DateTimeField(
        blank=False,
        verbose_name=("Дата и время публикации"),
        help_text=("Если установить дату и время в будущем "
                   "— можно делать отложенные публикации.")
    )
    author = models.ForeignKey(
        User,
        verbose_name=("Автор публикации"),
        on_delete=models.CASCADE,
        blank=False
    )
    location = models.ForeignKey(
        Location,
        verbose_name=("Местоположение"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name=("Категория"),
        on_delete=models.SET_NULL,
        null=True
    )
    is_published = models.BooleanField(
        default=True, blank=False, verbose_name=("Опубликовано"))
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, verbose_name=("Добавлено"))

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return self.title
