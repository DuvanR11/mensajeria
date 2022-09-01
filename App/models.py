from django.db import models
from django.utils.html import format_html

# Create your models here.
class Costumer(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Read', 'Read'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email =  models.CharField(max_length=30)
    subject =  models.CharField(max_length=25)
    message = models.TextField(max_length=500)
    file = models.FileField(upload_to='foto')
    status = models.CharField(max_length=12, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # control de respuesta leidas/no leidas
    def situation(self):
        if self.status == 'Read':
            return format_html('<span style="color:black">{0}</span>', self.status)
        else:
            return format_html('<span style="color:red">{0}</span>', self.status)
    situation.allow_tags = True
    
    def __str__(self):
        return self.name