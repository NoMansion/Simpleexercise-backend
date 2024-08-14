from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload-cv/', views.UploadCVView.as_view(), name='upload-cv'),
    path('upload/', views.NoteUploadView.as_view(), name='note-upload'),
    path('note/<int:note_id>/', views.RetrieveNoteView.as_view(), name='retrieve_note'),
    path('latest-note/', views.LatestNoteView.as_view(), name='latest-note'),
    path('notes/<int:pk>/', views.NoteUpdateView.as_view(), name='note-update'),
    path('latest-note/complete/', views.NoteComplete.as_view(), name='complete'),
    path('latest-note/delete/', views.NoteDeleteView.as_view(), name='note_delete'),
]
