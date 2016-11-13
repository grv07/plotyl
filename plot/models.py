from django.db import models
from django.forms import ModelForm

class Phone(models.Model):
    """Phone Class to handle phone data from api call"""    
    pos_x = models.FloatField(default=0) 
    pos_y = models.FloatField(default=0)
    rssi = models.FloatField(default=0)
    time = models.FloatField(default=0)
    imsi = models.CharField(max_length=30, blank=False)

    def save(self, *args, **kwargs):
        # Code to custom save
        super(Phone, self).save(*args, **kwargs)


class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'    

# Create your models here.
