from django.db import models
from django.contrib.auth.models  import User
# Create your models here.


class BookInfo(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    published_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,related_name='books',on_delete=models.CASCADE)