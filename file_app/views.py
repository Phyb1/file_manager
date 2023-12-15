from django.shortcuts import render, redirect
from django.http import FileResponse
from .forms import UploadFileForm
from .models import  UploadFile

# Create your views here.

def file_list(request):
    files =UploadFile.objects.all()
    return render(request, 'file_list.html', {'files':files})


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = UploadFileForm()
        return render(request, 'upload_file.html', {'form':form})
        

def download_file(request, file_id):
    uploaded_file =UploadFile.objects.get(pk=file_id)
    response = FileResponse(uploaded_file.file, as_attachment=True)
    return response


