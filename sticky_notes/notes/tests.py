# notes/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Note
from .forms import NoteForm

"""
Test suite for the Sticky Notes application.

This module contains tests for the Note model, NoteForm, and views related to
note creation, update, deletion, and listing/reading.
"""


class NoteModelTests(TestCase):
    """
    Tests for the Note model in the Sticky Notes application.
    """

    def setUp(self):
        """
        Create a test note instance for use in the tests.
        """
        self.note = Note.objects.create(
            title="Test Note", content="This is a test note."
        )

    def test_note_str(self):
        """
        Test the string representation of the Note model.
        """
        self.assertEqual(str(self.note), "Test Note")

    def test_note_creation(self):
        """
        Test the creation of a Note instance.
        """
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "This is a test note.")


class NoteFormTests(TestCase):
    """
    Tests for the NoteForm used in the Sticky Notes application.
    """

    def test_valid_note_form(self):
        """
        Test that the form is valid with correct data.
        """
        form_data = {"title": "New Note", "content": "This is a new note."}
        form = NoteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_note_form_empty(self):
        """
        Test that the form is invalid when no data is provided.
        """
        form = NoteForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)  # Both fields are required


class NoteViewTests(TestCase):
    """
    Tests for the views in the Sticky Notes application.
    """

    def setUp(self):
        """
        Set up a test note and create a user for testing.
        """
        self.note = Note.objects.create(
            title="Test Note", content="This is a test note."
        )

    def test_note_list_view(self):
        """
        Test the note list view to ensure it displays notes correctly.
        """
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_list.html")
        self.assertContains(response, "Test Note")
        self.assertQuerysetEqual(response.context["notes"], [self.note])

    def test_note_create_view(self):
        """
        Test the create note view.
        """
        response = self.client.post(
            reverse("note_create"),
            {"title": "New Note", "content": "New note content."},
        )
        # Check for redirect after successful creation
        self.assertEqual(response.status_code, 302)
        # Ensure note was created
        self.assertTrue(Note.objects.filter(title="New Note").exists())

    def test_note_update_view(self):
        """
        Test the update note view.
        """
        response = self.client.post(
            reverse("note_update", args=[self.note.pk]),
            {"title": "Updated Note", "content": "Updated content."},
        )
        # Check for redirect after successful update
        self.assertEqual(response.status_code, 302)
        # Refresh note instance from database
        self.note.refresh_from_db()
        # Check title was updated
        self.assertEqual(self.note.title, "Updated Note")
        # Check content was updated
        self.assertEqual(self.note.content, "Updated content.")

    def test_note_delete_view(self):
        """
        Test the delete note view.
        """
        response = self.client.post(
            reverse("note_delete", args=[self.note.pk])
            )
        # Check for redirect after deletion
        self.assertEqual(response.status_code, 302)
        # Ensure note was deleted
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
