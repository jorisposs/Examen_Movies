from django.db import models

# Create your models here.
class Movie(models.Model):
	movie_name = models.CharField(max_length=50)
		
	def __unicode__(self):
		return self.movie_name

class Actor(models.Model):
	actors_name = models.CharField(max_length=300)
	movie_actor = models.ForeignKey(Actor)
	
	def __unicode__(self):
		return self.actor_name