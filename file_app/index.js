document.querySelectorAll('.sort').forEach(function (element) {
    element.addEventListener('click', function (event) {
        event.preventDefault();
        var sortBy = this.getAttribute('data-sort-by');
        window.location.href = '{% url "file_app:file_list" %}?sort_by=' + sortBy;
    });
});
