from django.db import models

# Create your models here.

class Directory(models.Model):
	base = models.TextField()
	cur = models.TextField()
	added = models.TextField()
	def __str__(self):
		return self.base