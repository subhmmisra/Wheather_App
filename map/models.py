from django.db import models

class Location(models.Model):
	name = models.CharField(
		max_length=50,
		null=False,
		blank=False,
		unique=True)
	lat = models.FloatField(
		null=False)
	lng = models.FloatField(
		null=False)

	def __str__(self):
		return self.name

	@property
	def serialize(self):
		return {
		"lat": self.lat,
		"lng": self.lng,
		"name": self.name}

