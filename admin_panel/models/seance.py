from django.db import models
from django.utils import timezone

from admin_panel.models.cinema_hall import Hall
from admin_panel.models.film import Film


class Seance(models.Model):
    class FormatType(models.TextChoices):
        TWO_D = "2D", "2D"
        DBOX = "DBOX", "DBOX"
        VIP = "VIP", "VIP"

    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name="seances",
    )
    hall = models.ForeignKey(
        Hall,
        on_delete=models.CASCADE,
        related_name="seances",
    )
    datetime = models.DateTimeField(default=timezone.now)
    format_type = models.CharField(
        max_length=10,
        choices=FormatType.choices,
        default=FormatType.TWO_D
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.film.title} in {self.hall.title} at {self.datetime}"

    class Meta:
        ordering = ["datetime"]
        verbose_name = "Seance"
        verbose_name_plural = "Seances"
