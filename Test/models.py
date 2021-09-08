from django.db import models

# Create your models here.
class Registrartion(models.Model):
    userid = models.IntegerField()
    #id = models.IntegerField()
    tittle= models.TextField(max_length=100)
    body=models.TextField()


    
    
