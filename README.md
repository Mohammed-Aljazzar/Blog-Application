# Blog App

## Description
The Blog App is a Django-based web application designed to create, manage, and share blog posts. It provides a user-friendly interface for writing posts, adding comments, and sharing content via email. Built with modern web technologies, the app features a responsive design powered by Bootstrap, ensuring accessibility across devices. The application integrates a dark-themed UI, secure email functionality using Gmail SMTP, and pagination for an organized post display. Whether you're a blogger or a developer looking to explore Django, this app serves as a robust starting point.

## Features

- **Post Management:**
  - Create, view, and share blog posts with a clean, card-based layout.
  - Dynamic post titles, publication dates, and author attribution.

- **Responsive Design:**
  - Built with Bootstrap 5 for a mobile-friendly experience.
  - Dark theme (bg-dark text-light) with hover effects and a sleek sidebar.

- **Comment System:**
  - Add and display comments on individual posts.
  - Comment count with pluralization support (e.g., "1 comment" vs. "2 comments").

- **Email Sharing:**
  - Share posts via email using a custom form (EmailPostForm).
  - Configured with Gmail SMTP and secure App Password authentication.

- **Security:**
  - Environment variable management with python-decouple for sensitive data (e.g., email credentials).
  - CSRF protection for forms.

## Requirements
- Python 3.13+
- Django 5.0.11
- Bootstrap 5.3 (via CDN)
- Font Awesome 6.0 (via CDN)
- python-decouple for environment variables
- Install dependencies with:
bash
```
pip install django python-decouple
```

## Installation

1. **Clone the Repository:**
```
git clone https://github.com/yourusername/blog-app.git
cd blog-app
```

2. **Set Up Virtual Environment:**
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**
```
pip install -r requirements.txt
```

4. **Configure Environment Variables:**
  - Create a .env file in the project root:
```
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL="Your Name <your-email@gmail.com>"
```
Generate an App Password from Google Account Settings if using Gmail SMTP.

5. **Apply Migrations:**
```
python manage.py makemigrations
python manage.py migrate
```

6. **Run the Server:**
```
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser.






