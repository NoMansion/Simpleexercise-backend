import base64
import logging
from urllib import request, response
from django.db import models
from django.core.files.base import ContentFile
import json

logger = logging.getLogger(__name__)

class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField(default="nameless")
    cv = models.FileField(upload_to='cvs/', null=True, blank=True)
    binary = models.BinaryField(null=True, blank=True)
    numDays = models.IntegerField(default=-1)
    length = models.TextField(default="no length given")
    focus = models.TextField(default="no focus specified")
    workoutPlan = models.TextField(default="no workout plan")
    completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Call the parent save method
        super(Note, self).save(*args, **kwargs)

        # Update the binary field if cv is not empty
        if self.cv:
            # Ensure the file has been saved before accessing it
            if self.cv.file:
                # Read the content of the file
                self.binary = self.cv.read()
                # Save the updated Note instance
                super(Note, self).save(update_fields=['binary'])
