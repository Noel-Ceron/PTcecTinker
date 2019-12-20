from django.db import models

# Create your models here.
class operacion(models.Model):
    comando=models.IntegerField(default=0)
    
    def __str__(self):
        return "%d"%(self.comando)
        
        
class operacion_vol(models.Model):
    comando=models.CharField(max_length = 4)
    
    def __str__(self):
        return "%d"%(self.comando)
    
