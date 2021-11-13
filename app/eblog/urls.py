from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

app_name = 'eblog'

urlpatterns = [
    path('notes/', views.NotesView.as_view(), name='notes'),
    # path('note/<int:note_id>/', views.NoteDetailView.as_view(), name='note'),
    # path('note/add/', views.NoteEditorView.as_view(), name='add'),
    # path('note/<int:note_id>/save/', views.NoteEditorView.as_view(), name='save'),
    ]