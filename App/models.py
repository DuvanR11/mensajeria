from django.db import models
from django.utils.html import format_html
from django.utils import timezone

# Create your models here.
STATUS_CHOICES = (
    ("Pending", "Pending"),
    ("Read", "Read"),
)


class Costumer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email =  models.CharField(max_length=30)
    subject =  models.CharField(max_length=25)
    message = models.TextField(max_length=1001)
    file = models.FileField(upload_to='foto')
    created_at = models.DateTimeField(auto_now_add=True)
    estado = models.CharField( 
        max_length = 20, 
        choices = STATUS_CHOICES, 
        default = 'Pending'
        ) 
    
    # control de respuesta leidas/no leidas
    def situation(self):
        if self.estado == 'Read':
            return format_html('<span style="color:green">{0}</span>', self.estado)
        else:
            return format_html('<span style="color:red">{0}</span>', self.estado)
    situation.allow_tags = True
    
    def __str__(self):
        return self.name
    
