from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=100000000)
    # content = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now(), blank=True)
    # date_posted = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
        # return self.title
    