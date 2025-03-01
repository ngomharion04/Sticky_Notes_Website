# notes/forms.py
from django import forms
from .models import Note

"""
Forms for the Sticky Notes application.

This module defines the NoteForm class, which is used for creating and updating
notes in the application. The form is based on the Note model.
"""


class NoteForm(forms.ModelForm):
    """
    A form for creating and updating Note instances.

    Fields:
    - title: CharField
    - content: TextField

    Meta class:
    - Define the model to use (Note) and the fields to include in the form.

    This form uses Django's ModelForm to automatically generate form fields
    based on the Note model attributes `title` and `content`.
    """

    class Meta:
        # Specify the model associated with this form
        model = Note
        fields = ["title", "content",]
