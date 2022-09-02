from django.contrib import admin
from .models import *

# Register your models here

class CostumerAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'name', 'phone', 'email', 'subject', 'message', 'file', 'created_at']
    list_display = ['name', 'phone', 'email', 'subject', 'created_at', 'file', 'situation']
    search_fields = ['name', 'phone', 'email', 'subject']
    list_filter = ['estado']
    list_per_page: 10
    

    
admin.site.register(Costumer, CostumerAdmin)
