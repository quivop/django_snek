# adding this so custom method in Fanfic will work
import datetime

from django.db import models

# adding this to support custom method in Fanfic as well
from django.utils import timezone 


## mah first models~ ##

class Fanfic(models.Model):
	title = models.CharField('fanfic title', max_length=100)
	text = models.TextField('fanfic text')
	pub_date = models.DateTimeField('date published')
	
	# adding a helpful representation of this object
	# so that it doesn't return gibberish in the API??
	def __str__(self):
		return self.title

	# and a custom method now:
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Link(models.Model):
	fanfic = models.ForeignKey(Fanfic, on_delete=models.CASCADE)
	text = models.CharField('link text', max_length=150)
	url = models.CharField('link URL', max_length=255)

	# adding helpful representation of this object i guess
	# as well
	def __str__(self):
		return self.text
