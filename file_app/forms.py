from django import forms
from .models import UploadFile

class UploadFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'readonly': True})  # Set title field as read-only
        self.fields['title'].help_text = "Automatically set to the filename."

    class Meta:
        model = UploadFile
        fields = ("title", 'file',)
