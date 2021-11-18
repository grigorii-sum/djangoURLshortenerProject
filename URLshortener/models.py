from django.db import models

from .utils import create_short_url


class Shortener(models.Model):
    url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    hit_counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.url) + ' to ' + self.short_url

    '''
    Overriding "save" function for:
    - creating short URL for Shortener instance (at first time)
    - OR just saving new number in "hit_counter" field
    '''
    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_short_url(self)

        super().save(*args, **kwargs)
