from django.db import models

# Create your models here.

class Member(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 50)
	link = models.CharField(max_length = 50)
	abstract = models.CharField(max_length = 300, default = "")
	ctype = models.IntegerField(default = 0)
	def __str__(self):
		return self.name

class Project(models.Model):
	title = models.CharField(max_length = 1000)
	responsible = models.ForeignKey(Member)
	funded = models.CharField(max_length = 100)
	abstract = models.CharField(max_length = 5000)
	def __str__(self):
		return self.title

class Member_Project(models.Model):
	part = models.ForeignKey(Member)
	proj = models.ForeignKey(Project)
	def __str__(self):
		return self.proj.title