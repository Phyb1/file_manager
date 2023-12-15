from django.db import models

# Create your models here.
class UploadFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/')
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

