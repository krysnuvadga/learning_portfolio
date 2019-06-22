from django.db import models
from django.urls import reverse

# Create your models here
class Link(models.Model):
    """docstring for Link."""

    url = models.URLField()

    @staticmethod
    def shorten(link):

        '''Method to create url get or create url object'''

        l, _ = Link.objects.get_or_create(url=link.url)
        return str(l.pk)


    @staticmethod
    def expand(slug):

        ''' Method to reverse short url to it original length '''

        link_id = int(slug)
        l = Link.objects.get(pk=link_id)
        return l.url

    def get_absolute_url(self):
        return reverse("link_show", kwargs={'pk': self.pk})
