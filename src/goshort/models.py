from django.db import models

# Create your models here.

class ShortenURL(models.Model):
    url = models.CharField(max_length=250,)
    shorturl = models.CharField(max_length=15, unique=True)
    # if you already have some data with field and then you add another field in database
    # shorturl = models.CharField(max_length=15, null=True) # emty in database is ok
    # or
    # shorturl = models.CharField(max_length=15, default='abcd')
    # or you can delete database and regenerate

    def __str__(self):
        return str(self.url)
    # this return function is to show the added data as a list on web app
    # to show the primary key or primary id
    # return str(self.id)
    # return str(self.pk)
    # id and pk will be autogenerated by django

    # for python2
    def __unicode__(self):
        return str(self.url)