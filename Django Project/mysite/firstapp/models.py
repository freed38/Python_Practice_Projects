from django.db import models

class Locations(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256)
    desc = models.TextField("Description")
    url = models.CharField(max_length=1024)
    address = models.CharField(max_length=1024)
    image_url = models.CharField(max_length=1024)





