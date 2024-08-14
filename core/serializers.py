import logging
from venv import logger
from rest_framework import serializers


from .models import Note
from rest_framework import serializers

logger = logging.getLogger(__name__)

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"

class CVUploadSerializer(serializers.Serializer):
    note_id = serializers.IntegerField()
    uploaded_file = serializers.FileField()

    def save(self):
        note_id = self.validated_data['note_id']
        uploaded_file = self.validated_data['uploaded_file']

        note = Note.objects.get(id=note_id)
        # Save the file and its binary content
        note.cv.save(uploaded_file.name, uploaded_file, save=False)
        note.binary = uploaded_file.read()
        note.save()
        return note
