from django.db import models

# Create your models here.
class Distrib(models.Model):
	name = models.CharField(max_length = 100)
	owner = models.CharField(max_length = 100)
	address = models.CharField(max_length = 500)
	country = models.CharField(max_length = 500)
	state = models.CharField(max_length = 500)
	city = models.CharField(max_length = 500)
	phone = models.DecimalField(max_digits = 10, decimal_places = 0)
	email = models.CharField(max_length = 100)

	def __str__(self):
		return self.name
