from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View
from django.http import FileResponse
from django.core.paginator import Paginator
from .forms import UploadFileForm
from .models import UploadFile
from django.http import JsonResponse
 
class FileListView(ListView):
    model = UploadFile
    template_name = 'file_list.html'
    context_object_name = 'files'
    paginate_by = 10  # Number of files per page
    ordering = ['upload_date']  # Default ordering (by upload date)

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'date':
            queryset = queryset.order_by('-upload_date')  # Sort by upload date (descending)
        elif sort_by == 'file_type':
            queryset = queryset.order_by('file')  # Sort by file type
        elif sort_by == 'size':
            queryset = queryset.annotate(file_size=F('file__size')).order_by('file_size')  # Sort by file size
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['files'], self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context


class FileDownloadView(View):
    def get(self, request, file_id):
        uploaded_file = get_object_or_404(UploadFile, pk=file_id)
        try:
            response = FileResponse(uploaded_file.file, as_attachment=True)
            return response
        except FileNotFoundError:
            return render(request, 'error.html', {'message': 'File not found.'})
        except Exception as e:
            return render(request, 'error.html', {'message': f'An error occurred: {str(e)}'})

class FileUploadView(View):
    def get(self, request):
        form = UploadFileForm()
        return render(request, 'upload_file.html', {'form': form})

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_app:file_list')
        return render(request, 'upload_file.html', {'form': form})


def get_upload_progress(request):
    if 'upload_progress' in request.session:
        progress = request.session['upload_progress']
    else:
        progress = 0
    return JsonResponse({'progress': progress})
