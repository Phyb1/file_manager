from django.urls import path
from .import views
app_name ='file_app'
urlpatterns = [
    path('', views.FileListView.as_view(), name='file_list'),
    path('upload/', views.FileUploadView.as_view(), name='upload'),
    path('download/<int:file_id>/', views.FileDownloadView.as_view() ,name='download'),
path('get_upload_progress/', views.get_upload_progress, name='get_upload_progress'),]
