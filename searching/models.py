from django.db import models

# Create your models here.

class Crawler(models.Model):
    n_docs = models.IntegerField(null=True, blank=True)
    in_degree = models.IntegerField(null=True, blank=True)
    out_degree = models.IntegerField(null=True, blank=True)
    starting_url = models.TextField(null=True, blank=True)


class Indexing(models.Model):
    direction = models.CharField(max_length=150, null=True, blank=True)
