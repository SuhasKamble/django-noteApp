from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.note, name='Note'),
    path("note", views.createNote, name='CreateNote'),
    path("<str:slug>", views.deleteNote, name='DeleteNote'),

]
