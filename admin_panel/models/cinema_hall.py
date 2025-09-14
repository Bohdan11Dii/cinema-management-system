from django.db import models
from django.utils import timezone

from admin_panel.models.image import ImageTitle
from admin_panel.models.seo import SeoBlock


class Cinema(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    condition = models.TextField(blank=True)
    logo_cinema = models.ImageField(upload_to="cinema_logos/", null=True, blank=True)
    banner_cinema = models.ImageField(upload_to="cinema_banners/", null=True, blank=True)
    collection = models.ForeignKey(
        ImageTitle,
        on_delete=models.CASCADE,
        related_name="cinemas",
        blank=True,
        null=True,
    )
    seo_cinema = models.ForeignKey(
        SeoBlock,
        on_delete=models.CASCADE,
        related_name="cinemas",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Cinema"
        verbose_name_plural = "Cinemas"


class Hall(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    logo_hall = models.ImageField(upload_to="hall_logos/", null=True, blank=True)
    banner_hall = models.ImageField(upload_to="hall_banners/", null=True, blank=True)
    collection = models.ForeignKey(
        ImageTitle,
        on_delete=models.CASCADE,
        related_name="halls",
        blank=True,
        null=True,
    )
    seo_hall = models.ForeignKey(
        SeoBlock,
        on_delete=models.CASCADE,
        related_name="halls",
        blank=True,
        null=True,
    )
    cinema = models.ForeignKey(
        Cinema,
        on_delete=models.CASCADE,
        related_name="halls",
    )
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Hall"
        verbose_name_plural = "Halls"
