from django.db import models

class User(models.Model):
  email = models.CharField(max_length=50)
  pwd = models.CharField(max_length=100)
  name = models.CharField(max_length=10)

class Article(models.Model):
  title = models.CharField(max_length=100)
  content = models.CharField(max_length=1000)
  time = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
class FileAttach(models.Model):
  o_filename = models.CharField(max_length = 1000)
  save_filename = models.CharField(max_length = 1000)
  filesize = models.IntegerField(default = 0)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)