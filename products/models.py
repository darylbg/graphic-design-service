from django.db import models

# Create your models here.
TYPE_CHOICES = (
    ('100', 'poster'),
    ('50', 'logo'),
    ('20', 'icon'),
)

POSTER_SIZE_CHOICES = (
    ('10', '1080 x 1920'),
    ('20', '1080 x 1080'),
)

QUANTITY_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
)

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='poster')
    size = models.CharField(max_length=15, choices=POSTER_SIZE_CHOICES, default='1080 x 1920')
    quantity = models.CharField(max_length=12, choices=QUANTITY_CHOICES, default='1')


    def __str__(self):
        return self.name
