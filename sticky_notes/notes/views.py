# notes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

"""
Views for the Sticky Notes application.

This module contains the view functions that handle requests related to notes,
including listing, creating, updating, and deleting notes.
"""


def note_list(request):
    """
    View function to display a list of all notes.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered template displaying all notes.
    """
    notes = Note.objects.all()  # Retrieve all notes from the database
    return render(request, "notes/note_list.html", {"notes": notes})


def note_create(request):
    """
    View function to create a new note.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered template for note creation or redirect to note list
        upon successful creation.
    """
    if request.method == "POST":
        # Create a form instance with the submitted data
        form = NoteForm(request.POST)
        if form.is_valid():
            # Save the new note to the database
            form.save()
            return redirect("note_list")
    else:
        # Initialize an empty form
        form = NoteForm()
    return render(
        request, "notes/note_form.html", {"form": form}
    )  # Render the form template


def note_update(request, pk):
    """
    View function to update an existing note.

    Args:
        request: The HTTP request object.
        pk: The primary key of the note to be updated.

    Returns:
        Rendered template for note update or redirect to note
        list upon successful update.
    """
    # Retrieve the note or return a 404 error
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()  # Save the updated note to the database
            return redirect("note_list")
    else:
        # Initialize the form with the existing note data
        form = NoteForm(instance=note)
    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    """
    View function to delete a specific note.

    Args:
        request: The HTTP request object.
        pk: The primary key of the note to be deleted.

    Returns:
        Rendered template for deletion confirmation or redirect to note
        list upon successful deletion.
    """
    # Retrieve the note or return a 404 error
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()  # Delete the note from the database
        return redirect("note_list")
    return render(request, "notes/note_confirm_delete.html", {"note": note})
