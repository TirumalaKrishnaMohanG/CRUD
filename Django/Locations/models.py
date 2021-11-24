from django.db import models

# Create your models here.
class locations(models.Model):
	location = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	country = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "locations"
