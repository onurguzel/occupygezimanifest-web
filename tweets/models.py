from django.db import models


class Tweet(models.Model):
    text = models.CharField(max_length=140)
    url = models.URLField(unique=True)

    def get_twitter_username(self):
        from urlparse import urlparse
        return urlparse(self.url).path.split('/')[1]

    def __unicode__(self):
        return unicode(self.text)
