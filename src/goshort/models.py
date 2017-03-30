from django.db import models

# Create your models here.

class ShortenURL(models.Model):
    url = models.CharField(max_length=250,)

    def __str__(self):
        return str(self.url)

    # for python2
    def __unicode__(self):
        return str(self.url)
