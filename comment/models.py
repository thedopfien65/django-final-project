from django.db import models

class Comment(models.Model):
    comment_text = models.CharField(max_length = 250)
    comment_author = models.CharField(max_length = 40)
    comment_date = models.DateTimeField('date published')
    comment_rating = models.IntegerField()