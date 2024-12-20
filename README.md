# my_website

A simple Django-based web application for posting and displaying images with titles. Users can upload posts, view details, and browse through previously uploaded posts. The project uses Django for the backend and Bootstrap for frontend styling.

## Features

- Upload and display posts with images and titles.
- View post details with full-size images.
- Responsive design using Bootstrap.
- Basic messages for form submission feedback.

## Requirements

- Python 3.x
- Django 5.x
- `sorl.thumbnail` for image handling
- `Bootstrap 5` for frontend styling

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DvirUliel/Django-Posts-Feed-Server.git
2. Navigate to the project directory:
   ```bash
   cd Django-Posts-Feed-Server
3. Set up a virtual environment:
   ```bash
   pip install pipenv
   pipenv shell
4. Install dependencies:
   ```bash
   pip install django
   pip install sorl-thumbnail
5. Run migrations to set up the database:
   ```bash
   python manage.py migrate
6. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
7. Start the development server:
   ```bash
   python manage.py runserver 0.0.0.0:8000
8. Visit localhost:8000 to access the application in your browser.




