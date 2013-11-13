from django.db import models


class Image(models.Model):
    path = models.CharField('Filepath', max_length=1024)
