from django import forms
from .models import Profile

class AccountProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image', 'bio', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county')
