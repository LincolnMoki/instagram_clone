from django import forms
from . models import Image,Profile,Comments

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile','likes','comments','user']
class ImageProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]        