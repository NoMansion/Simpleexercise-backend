import logging
from venv import logger
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# from .forms import NoteForm, CVUploadForm
import json

from .models import Note
from rest_framework import viewsets
from .serializers import CVUploadSerializer, NoteSerializer
from core import serializers

logger = logging.getLogger(__name__)

class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """
    queryset = Note.objects.all().order_by('-created')
    serializer_class = NoteSerializer

class UploadCVView(APIView):
    def post(self, request):
        serializer = CVUploadSerializer(data=request.data)
        if serializer.is_valid():
            note = serializer.save()
            note.save()
            print(f"File successfully uploaded and saved. Note ID: {note.id}")
            return Response({'status': 'success', 'note_id': note.id}, status=status.HTTP_201_CREATED)
        print(f"Serializer errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class NoteUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        #     return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
        # return Response({'status': 'error', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        # return redirect('/upload-cv')

def send_workout_plan(plan, request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.workoutPlan = plan
    note.save()
    return redirect('/notes')

class RetrieveNoteView(APIView):
    def get(self, request, note_id, format=None):
        try:
            note = Note.objects.get(id=note_id)
        except Note.DoesNotExist:
            return Response({'error': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = NoteSerializer(note, context={'request': request})
        return Response(serializer.data)

class LatestNoteView(APIView):
    def get(self, request):
        try:
            latest_note = Note.objects.latest('created')
            serializer = NoteSerializer(latest_note, context={'request': request})
            return Response(serializer.data)
        except Note.DoesNotExist:
            return Response({"detail": "No notes found."}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, *args, **kwargs):
        try:
            latest_note = Note.objects.latest('created')
        except Note.DoesNotExist:
            return Response({"detail": "No notes found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = NoteSerializer(latest_note, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NoteDeleteView(generics.DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def delete(self, request, *args, **kwargs):
        # Retrieve the note by its ID from kwargs
        note_id = kwargs.get('pk')
        try:
            note = Note.objects.get(id=note_id)
            note.delete()
            return Response({'message': 'Note deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Note.DoesNotExist:
            return Response({'error': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)

class NoteUpdateView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteComplete(APIView):
    def post(self, request):
        try:
            latest_note = Note.objects.latest('created')
            latest_note.completed = True
            latest_note.save()
            serializer = NoteSerializer(latest_note, context={'request': request})  # Added context here
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Note.DoesNotExist:
            return Response({'error': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)

