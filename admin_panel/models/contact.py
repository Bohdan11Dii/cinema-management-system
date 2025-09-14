from django.db import models
from django.utils import timezone

from admin_panel.models.seo import SeoBlock


class ContactPage(models.Model):
    title = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)
    seo = models.ForeignKey(
        SeoBlock,
        on_delete=models.CASCADE,
        related_name="contact_pages"
    )
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Pages"


class Contact(models.Model):
    title = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    coordinates = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    logo = models.ImageField(upload_to="contact_logos/", blank=True, null=True)
    page = models.ForeignKey(
        ContactPage,
        on_delete=models.CASCADE,
        related_name="contacts",
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
