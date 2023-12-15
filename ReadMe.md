# File Manager

File Manager is a Django-based web application that allows users to upload, download, and manage files efficiently.

## Features

- Upload files and store them in the system.
- View a list of uploaded files.
- Download files from the system.
- Basic file management capabilities.

## Getting Started

### Prerequisites

- Python (version 3.x recommended)
- Django (version 3.x recommended)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Phyb1/file_manager.git
    ```

2. Navigate to the project directory:

    ```bash
    cd file_manager
    ``

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```
    ```
    use python manage.py runserver 0.0.0.0:8000
    to acces the file via a network 
    ```
6. Access the application in your web browser at `http://127.0.0.1:8000/`.

### Usage

1. Navigate to the "Upload File" section to upload new files.
2. Visit the "File List" section to view and manage uploaded files.
3. Download files by clicking on the download link.

### Testing

Run the tests using the following command:

```bash
python manage.py test
