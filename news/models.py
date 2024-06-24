from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title
