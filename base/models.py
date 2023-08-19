from django.db import models
    
class Newsletters(models.Model):
    article_url = models.URLField(max_length=1000)
    image_url = models.URLField(max_length=1000)
    title = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    datetime = models.DateTimeField()
    
    def __str__(self):
        return f"{self.title}"