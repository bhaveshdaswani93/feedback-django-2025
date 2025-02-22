from django.db import models

# Create your models here.

class Review(models.Model):
  user_name = models.CharField(max_length=100)
  review = models.TextField()
  rating = models.IntegerField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user_name
