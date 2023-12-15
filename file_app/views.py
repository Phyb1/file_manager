from django.shortcuts import render, redirect
from django.http import FileResponse
from .forms import UploadFileForm
from .models import  UploadFile

# Create your views here.

def file_list(request):
    files =UploadFile.objects.all()
    return render(request, 'file_list.html', {'files':files})



