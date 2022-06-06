from distutils.command.upload import upload
from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField()
    image = models.ImageField(upload_to='img/')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()


# с полями id, name, price, image, release_date, lte_exists и slug. Поле id - должно быть основным ключом модели.