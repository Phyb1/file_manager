from django.db import models

class UploadFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    upload_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.file.name.split('/')[-1]  # Extract file name from file path
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
