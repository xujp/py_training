from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class bbs(models.Model):
	title = models.CharField(max_length=150,unique=True)
	category_option = (
	('linux','Linux BBS'),
	('python','PY bbs'))
	category = models.CharField(max_length=50,choices=category_option)
	content = models.TextField()
	view_count = models.IntegerField(default=0)
	comment_count = models.IntegerField(default=0)
	ranking = models.IntegerField(default=1001)
	author = models.ForeignKey(User)
	publish_date = models.DateField()
	modify_date = models.DateField()
	def __unicode__(self):
		return self.title
	
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    def __unicode__(self):
        return self.last_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    def __unicode__(self):
        return self.title
