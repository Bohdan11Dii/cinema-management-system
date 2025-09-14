from django.db import models
from django.utils import timezone
from admin_panel.models.image import ImageTitle
from admin_panel.models.seo import SeoBlock


class News(models.Model):
    class PageType(models.IntegerChoices):
        ACTION = 0, "Action"
        NEWS = 1, "News"

    title = models.CharField(max_length=255, unique=True)  # краще зробити унікальним
    description = models.TextField(blank=True)  # null не потрібен для TextField
    image = models.ImageField(upload_to="news/", blank=True, null=True)  # зробив опціональним
    collection = models.ForeignKey(
        ImageTitle,
        on_delete=models.CASCADE,
        related_name="news",
        blank=True,
        null=True
    )
    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    link_url = models.URLField(blank=True, null=True)  # зробив не обов’язковим
    seo_news = models.ForeignKey(
        SeoBlock,
        on_delete=models.CASCADE,
        related_name="news",
        blank=True,
        null=True
    )
    type_page = models.IntegerField(choices=PageType.choices, default=PageType.NEWS)

    class Meta:
        ordering = ["-published_date"]  # останні новини зверху
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
