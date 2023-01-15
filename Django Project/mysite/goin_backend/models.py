from django.db import models

class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256)
    desc = models.TextField("Description")
    url = models.CharField(max_length=1024)
    address = models.CharField(max_length=1024)
    image_url = models.CharField(max_length=1024)

class GenreTag (models.Model): 
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)

class Band (models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=512)
    desc = models.TextField(null=True) 
    url = models.CharField(max_length=1024,null=True)
    image_url = models.CharField(max_length=1024,null=True)

class Event (models.Model):
    id = models.IntegerField(primary_key=True)
    band_id = models.ForeignKey(Band, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    desc = models.TextField(null=True)
    url = models.CharField(max_length=1024,null=True)
    image_url = models.CharField(max_length=1024,null=True)
    ticket_url = models.CharField(max_length=1024,null=True)
    start_datetime = models.DateTimeField
    finish_datetime = models.DateTimeField(null=True)
    verified = models.BooleanField
    price = models.DecimalField






