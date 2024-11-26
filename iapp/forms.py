from .models import UploadImage
from django import forms
class UserImage(forms.ModelForm):
    class Meta:
        model=UploadImage
        fields='__all__'

