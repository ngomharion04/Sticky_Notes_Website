# notes/models.py
from django.db import models

"""
Models for the Sticky Notes application.

This module defines the Note model, which represents a note in the application.
Each note has a title, content, and a timestamp for when it was created.
"""


class Note(models.Model):
    """
    Represents a note in the Sticky Notes application.

    Attributes:
        title (str): The title of the note, limited to 255 characters.
        content (str): The content of the note, stored as text.
        created_at (datetime): The timestamp for when the note was created,
                               automatically set when the note is created.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    # Timestamp of creation
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the Note object.

        This method is called when the Note object is printed or converted to
        a string. It returns the title of the note.
        """
        return self.title
