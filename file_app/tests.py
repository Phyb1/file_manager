
from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import UploadFile

class FileAppTests(TestCase):
    def setUp(self):
        self.uploaded_file = SimpleUploadedFile(
            "test_file.txt", b"File content."
        )

    def test_upload_file_view(self):
        # Ensure the upload_file view returns a 200 status code on GET request
        response = self.client.get(reverse('file_app:upload'))
        self.assertEqual(response.status_code, 200)

       
    def test_file_list_view(self):
        # Ensure the file_list view returns a 200 status code
        response = self.client.get(reverse('file_app:file_list'))
        self.assertEqual(response.status_code, 200)

    def test_download_file_view(self):
        # Upload a file
        uploaded_file = UploadFile.objects.create(file=self.uploaded_file)

        # Ensure the download_file view returns a 200 status code
        response = self.client.get(reverse('file_app:download', args=[uploaded_file.id]))
        self.assertEqual(response.status_code, 200)

    def test_nonexistent_file_download(self):
        # Ensure trying to download a non-existent file returns a 404 status code
        response = self.client.get(reverse('file_app:download', args=[999]))
        self.assertEqual(response.status_code, 404)
