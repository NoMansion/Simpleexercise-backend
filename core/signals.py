from urllib import request
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from .models import Note
from django.db import models

# Use a global dictionary to store string fields
string_fields = {}

@receiver(post_save, sender=Note)
def extract_string_fields(sender, instance, created, **kwargs):
    print("Signal triggered")  # Debug statement to check if the signal is triggered
    if created:
        for field in instance._meta.fields:
            if isinstance(field, (models.CharField, models.TextField)):
                string_fields[field.name] = getattr(instance, field.name)

    string_fields['id'] = instance.id
    
    # Store the string fields in variables
    for field_name, field_value in string_fields.items():
        print(f"{field_name} = {field_value}")  # Debug statement to print the field values
    
        
        