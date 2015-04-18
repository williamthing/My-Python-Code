# William Thing
# April 17, 2014
# First Django Web App!!!
# Poll App
#
# 

from django.db import models

class Question(models.Model):
	question_text = models.charField(max_length = 200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	question = models.ForeignKey(Question)				# each Choice is related to a single Question
	choice_text = models.charField(max_length = 200)
	votes = models.IntegerField(default = 0)





