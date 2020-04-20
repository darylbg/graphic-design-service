from django.db import models

# Create your models here.

TYPE_CHOICES = (
    ('poster', 'POSTER'),
    ('logo', 'LOGO'),
    ('icon', 'ICON'),
)

POSTER_SIZE_CHOICES = (
    ('1080 x 1920', '1080_X_1920'),
    ('1080 x 1080', '1080_X_1080'),
)


class CustomProduct(models.Model):

    type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='poster')
    size = models.CharField(max_length=15, choices=POSTER_SIZE_CHOICES, default='1080 x 1920')
    description = models.TextField()

    def __str__(self):
        return self.type, self.size, self.description
