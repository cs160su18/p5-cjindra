from django.db import models

class Group(models.Model):
	established = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
  
class Post(models.Model):
  title = models.CharField(max_length=200)
  text = models.CharField(max_length=2000)
  user = models.CharField(max_length=50)
  region = models.CharField(max_length=200)
  def __str__(self):
    return ""+self.title

class Answer(models.Model):
  text = models.CharField(max_length=2000)
  user = models.CharField(max_length=50)
  region = models.CharField(max_length=200)
  parent = models.ForeignKey(Post, on_delete=models.CASCADE)
  def __str__(self):
    return ""+self.user+": "+self.text