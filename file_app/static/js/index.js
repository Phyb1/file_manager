document.querySelectorAll('.sort').forEach(function (element) {
    element.addEventListener('click', function (event) {
        event.preventDefault();
        var sortBy = this.getAttribute('data-sort-by');
        window.location.href = '{% url "file_app:file_list" %}?sort_by=' + sortBy;
    });
});

document.getElementById('uploadForm').addEventListener('submit', function() {
    document.getElementById('uploadForm').style.display = 'none';
    document.getElementById('uploadProgress').style.display = 'block';

    var progressBar = document.getElementById('progressBar');
    var uploadMessage = document.getElementById('uploadMessage');
    var uploadBtn = document.getElementById('uploadBtn');
    uploadBtn.disabled = true;

    // Make an AJAX request to get progress info from the backend
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_upload_progress/', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var progress = JSON.parse(xhr.responseText);
            progressBar.style.width = progress + '%';
            uploadMessage.innerText = 'Uploading... ' + progress + '% complete';
            if (progress >= 100) {
                uploadBtn.disabled = false;
            }
        }
    };
    xhr.send();
});
