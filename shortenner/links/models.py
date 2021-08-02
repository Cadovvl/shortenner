from django.db import models

from django.contrib.auth.models import User

from links.tools import id_to_link

from shortenner.settings import SHORT_LINK_HOST_NAME

class Link(models.Model):
    link_id = models.IntegerField()
    author = models.ForeignKey(User, related_name='links', on_delete=models.CASCADE)
    url = models.URLField(max_length=200)

    def get_short_url(self):
        return SHORT_LINK_HOST_NAME + id_to_link(self.link_id)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['link_id'], name="unique_link")
        ]

