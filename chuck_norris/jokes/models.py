from django.db import models

# Create your models here.
class Joke(models.Model):
	joke = models.CharField(max_length=500)


	def __unicode__(self):
		return self.joke
