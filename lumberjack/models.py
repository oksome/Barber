from django.db import models


class Image(models.Model):
    path = models.CharField('Filepath')
