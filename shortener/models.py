from django.db import models

from .util import code_generator


# Create your models here.
class SqueezeURL(models.Model):
    url = models.CharField(max_length=220, )
    short_code = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.short_code is None or self.short_code == "":
            self.short_code = code_generator()
        super(SqueezeURL, self).save(*args, **kwargs)

    def __str__(self):
        return self.url

    def __unicode__(self):
        return self.url
