from django.db import models


class ImageTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    collection = models.ForeignKey(ImageTitle, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
