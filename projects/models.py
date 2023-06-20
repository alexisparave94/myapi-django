from django.db import models

# Create your models here.
class Projects(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField(default='')
  technology = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
