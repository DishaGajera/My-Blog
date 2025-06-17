# Django Blog Application

A simple yet functional blog web application built with Django. It includes user authentication, post creation, category-based filtering, and pagination. This project demonstrates Django best practices for models, views, forms, and templates.

## Features

- User registration and login
- Create and view blog posts
- Assign categories to posts (Health, Food, Recipes, Technology, Education, Sports, Entertainment)
- Filter posts by category
- Pagination for posts list
- Responsive UI using Tailwind CSS

## Technologies Used

- Python 3.9
- Django 4.2
- SQLite3 (default Django DB)
- Tailwind CSS for styling

## Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/DishaGajera/My-Blog.git
cd My-Blog


Create Virtual Environment & Activate

    python3 -m venv env
    source env/bin/activate

Install Dependencies

    pip install -r requirements.txt

Run Migrations

    python manage.py makemigrations
    python manage.py migrate

Create Superuser (optional)

    python manage.py createsuperuser

Preload Categories (run in Django shell)

    python manage.py shell

    from blog.models import Category
    categories = ['Health', 'Food', 'Recipes', 'Technology', 'Education', 'Sports', 'Entertainment']
    for name in categories:
        Category.objects.get_or_create(name=name)
    exit()

Run the Server

    python manage.py runserver
    Visit http://127.0.0.1:8000/ to use the app.

## Screenshots

Check the [`screenshots`](screenshots) folder for app images demonstrating the features and UI.


