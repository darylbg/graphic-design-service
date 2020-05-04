from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_image = models.ImageField(upload_to='images')
    bio = models.TextField()
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)

    def __str__(self):
        return self.profile_image, self.bio, self.phone_number, self.country, self.postcode, self.town_or_city, self.street_address1, self.street_address2, self.county
