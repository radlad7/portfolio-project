from django.db import models
import datetime
import pytz

# Create your models here.

# Create a Blog model
class Blog(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')

# My Draft:
# class Blog(models.Model):
#     title = models.CharField(max_length=50)
#     pub_date =models.DateField(auto_now=False)
#     body = models.TextField()
#     image = models.ImageField(upload_to='images/blog')

# Add the Blog app to the settings
    # 'blog.apps.BlogConfig',
# create a migration
    #python manage.py migrate

# Migrate
    #python manage.py makemigrate

# Add to the admin
    # from django.contrib import admin
    # from .models import Blog
    #
    # # Register your models here.
    # admin.site.register(Blog)
