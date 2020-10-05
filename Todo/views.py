from django.shortcuts import render, HttpResponse, redirect
from Todo.models import Note
# Create your views here.


def note(request):

    allNotes = Note.objects.all()
    context = {"allNotes": allNotes}

    return render(request, 'note.html', context)


def deleteNote(request, slug):
    Note.objects.filter(title=slug).delete()
    return redirect("/")


def createNote(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        msg = request.POST.get("msg")
        notes = Note(title=title, msg=msg)
        notes.save()
    return render(request, 'createnote.html')
