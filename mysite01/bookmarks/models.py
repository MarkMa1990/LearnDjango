from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=30)
	password = models.IntegerField()
	email	 = models.EmailField()

class Link(models.Model):
	url		 = models.URLField(unique=True)

class Bookmark(models.Model):
	title 	 = models.CharField(max_length=200)
	user 	 = models.ForeignKey(User)
	link 	 = models.ForeignKey(Link)