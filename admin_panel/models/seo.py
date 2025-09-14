from django.db import models


class SeoBlock(models.Model):
    url = models.URLField(unique=True, db_index=True)
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "seo_block"
        verbose_name = "Seo Block"
        verbose_name_plural = "Seo Blocks"
