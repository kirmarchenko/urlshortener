from django.db import models


class Shortened(models.Model):
    """Здесь описываем как будут храниться данные в БД """
    initial_url = models.CharField(max_length=1000)
    shortened = models.CharField(max_length=10, unique=True)
