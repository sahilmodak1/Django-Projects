from django.db import models

# Create your models here.
class Blog(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=100)
	publication_date = models.DateTimeField()
	body = models.TextField()

	# Displays title insteam of Blog object 1 in admin page
	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]

	def publication_date_pretty(self):
		return self.publication_date.strftime('%b %e %Y')