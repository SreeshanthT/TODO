from django.db import models

# Create your models here.

class ToDoList(models.Model):
    
    active_choices = (
        (True,'Active'),
        (False,'Inactive'),
    )
    
    task = models.CharField(max_length=100)
    date = models.DateField(null=True)
    description = models.TextField(null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(choices=active_choices,default=True)
    is_completed = models.BooleanField(default=False,choices=(
        (True,'Completed'),
        (False,'Not Completed'),
    ))
    