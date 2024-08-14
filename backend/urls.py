from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from core import views
from core.views import NoteComplete, RetrieveNoteView, UploadCVView

router = routers.DefaultRouter()
router.register(r'notes', views.NoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Include the router's URL patterns for the notes app
    path('notes/', include('rest_framework.urls', namespace='rest_framework')),
    path('notes/<int:note_id>/send_workout_plan', views.send_workout_plan, name='send_workout_plan'),
    path('latest-note/', views.LatestNoteView.as_view(), name='latest-note'),
    path('latest-note/complete/', NoteComplete.as_view(), name='complete'),
    path('upload-cv/', views.UploadCVView.as_view(), name='upload-cv'),
    path('notes/<int:note_id>/delete/', views.NoteDeleteView.as_view(), name='note_delete')
]                                                                                               
