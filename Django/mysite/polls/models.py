# William Thing
# April 17, 2014
# First Django Web App!!!
# Poll App
#
# Creates a database schema
# Creates a Python database-access API for accessing Question
# and Choice objects.

from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	question = models.ForeignKey(Question)				# each Choice is related to a single Question
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)





