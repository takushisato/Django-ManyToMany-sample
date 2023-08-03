from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)

    def __str__(self):
        return self.title
