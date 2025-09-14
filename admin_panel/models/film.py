from django.db import models
from admin_panel.models.image import ImageTitle
from admin_panel.models.seo import SeoBlock


class Film(models.Model):
    class ShowType(models.IntegerChoices):
        POSTER = 0, "Poster"
        IN_WHILE = 1, "In While"

    class FormatType(models.TextChoices):
        TWO_D = "2D", "2D"
        THREE_D = "3D", "3D"
        IMAX = "IMAX", "IMAX"

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    film_image = models.ImageField(upload_to="films/", null=True, blank=True)
    collection = models.ForeignKey(
        ImageTitle,
        on_delete=models.CASCADE,
        related_name="films",
        blank=True,
        null=True
    )
    link = models.URLField(blank=True, null=True)
    type_show = models.IntegerField(choices=ShowType.choices, default=ShowType.POSTER)
    seo_film = models.ForeignKey(
        SeoBlock,
        on_delete=models.CASCADE,
        related_name="films",
        blank=True,
        null=True
    )
    format_type = models.CharField(
        max_length=10,
        choices=FormatType.choices,
        default=FormatType.TWO_D
    )

    created_at = models.DateTimeField(auto_now_add=True)  # коли додано фільм
    updated_at = models.DateTimeField(auto_now=True)  # коли востаннє змінено

    def __str__(self):
        return self.title

    class Meta:
        db_table = "film"
        ordering = ["title"]
        verbose_name = "Film"
        verbose_name_plural = "Films"
