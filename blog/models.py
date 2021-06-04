from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=64, blank=False, null=False)
    content = models.CharField(max_length=10000, blank=True, null=False)

    def __str__(self):
        return f"{self.title}: {self.content}"