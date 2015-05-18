from django.db import models

# Create your models here.

class Member(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 50)
	link = models.CharField(max_length = 50)
	abstract = models.CharField(max_length = 300, default = "")
	ctype = models.IntegerField(default = 0)
	html = models.TextField(default = "")
	def __str__(self):
		return self.name

class Project(models.Model):
	title = models.CharField(max_length = 1000)
	responsible = models.ForeignKey(Member)
	rtype = models.IntegerField(default = 0)
	funded = models.CharField(max_length = 100)
	abstract = models.CharField(max_length = 5000)
	def __str__(self):
		return self.title

class Member_Project(models.Model):
	part = models.ForeignKey(Member)
	proj = models.ForeignKey(Project)
	def __str__(self):
		return self.proj.title

class Course(models.Model):
	name = models.CharField(max_length = 500)
	ctype = models.IntegerField(default = 0)
	link = models.CharField(max_length = 100)
	note = models.CharField(max_length = 100)
	def __str__(self):
		return self.name

class Tesis(models.Model):
	name = models.CharField(max_length = 1000)
	author = models.CharField(max_length = 500)
	title = models.CharField(max_length = 500)
	ttype = models.IntegerField(default = 0)
	status = models.IntegerField(default = 0)
	tutors = models.CharField(max_length = 500, default = "")
	def __str__(self):
		return self.author

class Tutor(models.Model):
	tutor = models.ForeignKey(Member)
	teg = models.ForeignKey(Tesis)
	def __str__(self):
		return self.tutor.name + " " + self.teg.name
