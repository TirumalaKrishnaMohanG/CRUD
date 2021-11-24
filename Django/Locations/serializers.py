#!/usr/bin/env python
# Headers
from rest_framework import serializers
from .models import locations

# Create a serializers
class locationsapiserializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = locations
		fields = '__all__'
