from django.db import models

class Phone(models.Model):
    """Phone Class to handle phone data from api call"""    
    pos_x = models.FloatField(default=0, editable=False) 
    pos_y = models.FloatField(default=0, editable=False)
    rssi = models.FloatField(default=0, editable=False)
    time = models.FloatField(default=0, editable=False)
    imsi =models.CharField(max_length=30, editable=False)

    def save(self, *args, **kwargs):
        # Code to custom save
        super(Phone, self).save(*args, **kwargs)

    # Validate before save. 
    def validate_data(self, **kwargs):
        pass
# Create your models here.
