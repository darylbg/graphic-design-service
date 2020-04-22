from django.db import models

# Create your models here.
TYPE_CHOICES = (
    ('POSTER', 'poster'),
    ('LOGO', 'logo'),
    ('ICON', 'icon'),
)

POSTER_SIZE_CHOICES = (
    ('1080_X_1920', '1080 x 1920'),
    ('1080_X_1080', '1080 x 1080'),
)

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='poster')
    size = models.CharField(max_length=15, choices=POSTER_SIZE_CHOICES, default='1080 x 1920')

    def __str__(self):
        return self.name
