from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from admin_panel.models.image import ImageTitle
from admin_panel.models.seo import SeoBlock


class MainPage(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    published_date = models.DateTimeField(default=timezone.now)
    phone_primary = PhoneNumberField()
    phone_secondary = PhoneNumberField()
    seo_description = models.TextField(blank=True, null=True)
    seo = models.ForeignKey(
        SeoBlock,
        on_delete=models.CASCADE,
        related_name="main_pages",
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_date"]
        verbose_name = "Main Page"
        verbose_name_plural = "Main Pages"


class SecondPage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to="second_page_images/", blank=True, null=True)
    collection = models.ForeignKey(
        ImageTitle,
        on_delete=models.CASCADE,
        related_name="second_pages",
    )
    seo = models.ForeignKey(
        SeoBlock,
        on_delete=models.CASCADE,
        related_name="second_pages",
    )
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-published_date"]
        verbose_name = "Second Page"
        verbose_name_plural = "Second Pages"
