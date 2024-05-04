from django.db import models
from django.core.validators import URLValidator


class Profile(models.Model):
    name = models.CharField(max_length=100, blank=False)
    github = models.URLField(validators=[URLValidator()], blank=False)
    linkedin = models.URLField(validators=[URLValidator()], blank=False)
    bio = models.TextField(blank=False, max_length=500)

    def __str__(self):
        return self.name
