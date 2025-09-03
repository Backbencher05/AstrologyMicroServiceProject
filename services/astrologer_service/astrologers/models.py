from django.db import models

class Astrologer(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.expertise})"
