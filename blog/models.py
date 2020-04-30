from django.db import models
from datetime import datetime

class Blog(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateTimeField(default=datetime.now)
    #last_updated = models.DateField(auto_now=True)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/', blank=True)


    def __str__(self):
        return self.title
