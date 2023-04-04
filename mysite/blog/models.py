from django.conf import settings
from django.db import models
from django.utils import timezone

# Inherit the model from django models
class Post(models.Model):

	# Remember that the attributes act as columns in the relational database
	
	# Create an attribute called author, which will be a "User" model. Now a link has been created
	# Between the "User" object and the "post" object, a link between data tables.
	# on_delete=models.CASCADE, means if the corresponding user to the Post is deleted, then the posts are deleted as well
	# NOTE: This cascade rule is one way, if posts are deleted the user won't be deleted.
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	
	# Attribute of a character field that'll be filled in and then shown 
	title = models.CharField(max_length=200)
	
	# Text field so no character limit 
	text = models.TextField()
	
	# Sets the date value to the date the post instance was created
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	
	# Sets the date of publication, then saves the post instance to the database;
	# Essentially, we're kind of rewriting and updating the instance in the database
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
	