from django import forms
from .models import locations
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class locationform(forms.ModelForm):
	class Meta:
		model = locations
		fields = [
			"location",
			"city",
			"country",
		]
