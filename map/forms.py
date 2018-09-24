from django import forms
from .models import Location as LocationModel

from django.core.exceptions import ValidationError
class LocationForm(forms.ModelForm):
	class Meta:
		model = LocationModel
		fields = '__all__'
	

