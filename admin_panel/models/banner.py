from django.db import models
from admin_panel.models.image import ImageTitle


class BackgroundBanner(models.Model):
    class BackgroundType(models.TextChoices):
        PHOTO = "photo", "Фото на фоні"
        COLOR = "color", "Просто фон"

    type = models.CharField(
        max_length=20,
        choices=BackgroundType.choices,
        default=BackgroundType.COLOR,
        verbose_name="Тип фону"
    )
    image = models.ImageField(
        upload_to="banners/backgrounds/",
        null=True,
        blank=True,
        verbose_name="Фонове зображення"
    )

    def __str__(self):
        return f"{self.get_type_display()} ({self.image.name if self.image else 'Без зображення'})"


class Banner(models.Model):
    class BannerType(models.TextChoices):
        MAIN = "main", "Головний"
        NEWS = "news", "Новини"

    type = models.CharField(
        max_length=20,
        choices=BannerType.choices,
        default=BannerType.MAIN,
        verbose_name="Тип банера"
    )
    collection = models.ForeignKey(
        ImageTitle,
        on_delete=models.CASCADE,
        related_name="banners",
        null=True,
        verbose_name="Колекція зображень"
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубліковано")
    rotation_speed = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Швидкість ротації (сек)"
    )

    def __str__(self):
        return f"{self.get_type_display()} - {self.collection.name if self.collection else 'Без колекції'}"
