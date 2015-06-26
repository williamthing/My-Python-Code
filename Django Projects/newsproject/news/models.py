from django.db import models

class Reporter(models.Model):
	full_name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.full_name

class Article(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateField()
	content = models.TextField()
	reporter = models.ForeignKey(Reporter)

	def __unicode__(self):
		return self.title