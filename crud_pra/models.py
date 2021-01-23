from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
  pub_date = models.DateField()

  def __str__(self):
    return self.title
