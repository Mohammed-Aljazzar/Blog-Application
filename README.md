# Blog App

## Description
The Blog App is a feature-rich Django web application designed for creating, managing, and sharing blog posts. It offers a modern, user-friendly interface for writing posts, adding comments, sharing content via email, and discovering content through advanced search and tagging. Built with Django 5.0.11, Bootstrap 5, and PostgreSQL, the app features a responsive, dark-themed UI, secure email integration, and SEO optimization with sitemaps and RSS feeds. 

## Features

- **Post Management:**
  - Create, view, and share blog posts with a clean, card-based layout.
  - Create, edit, and view blog posts with a clean, card-based layout.
  - Dynamic post titles, publication dates, author attribution, and status (Draft/Published).
  - Tag posts for categorization using the taggit library.
  - Display similar posts based on shared tags for enhanced content discovery.
  - Paginated post lists (3 posts per page) for organized browsing.

- **Comment System:**
  - Add and display comments on individual posts with name, email, and body fields.
  - Admin interface to toggle comment visibility (active/inactive).
  - Comment count with pluralization (e.g., "1 comment" vs. "2 comments").

- **Search Functionality:**
  - Advanced search using PostgreSQL's trigram similarity for typo-tolerant searches.
  - Search posts by title with weighted results, filtering results with similarity > 0.1.
  - Responsive search form with a modern design, including a search icon and full-width button.

- **Email Sharing:**
  - Share posts via email using a custom form (EmailPostForm).
  - Secure Gmail SMTP integration with App Password authentication.
  - CSRF protection for secure form submissions.

- **RSS Feed:**
  - Subscribe to the latest 5 published posts via an RSS feed.
  - Includes post title, truncated HTML description (30 words), and publication date.

- **SEO and Sitemap:**
  - SEO-friendly sitemap for published posts with weekly change frequency and 0.9 priority.
  - Updated timestamps for posts to improve search engine indexing.

- **Admin Interface:**
  - Comprehensive admin panel for managing posts and comments.
  - Post management: Filter by status, author, and publish date; search by title/body; prepopulate slugs from titles.
  - Comment management: Filter by active status and dates; search by name, email, and body.
  - Date hierarchy navigation and facet display for efficient admin workflows.

- **Responsive Design:**
  - Built with Bootstrap 5 for a mobile-first, responsive experience.
  - Light theme with a clean sidebar for navigation, search, and post highlights.
  - Hover effects, Font Awesome icons, and consistent color scheme (#007bff for primary, #28a745 for accents).

- **Security:**
  - Environment variable management with python-decouple for sensitive data (e.g., email credentials, database settings).
  - CSRF protection for all forms.
  - Secure PostgreSQL database configuration via Docker.

## Requirements
- Python 3.13+
- Django 5.0.11
- Docker and Docker Compose (for PostgreSQL)
- Bootstrap 5.3 (via CDN)
- Font Awesome 6.0 (via CDN)
- python-decouple for environment variables
- Required Python packages:
  - django
  - python-decouple
  - psycopg2-binary (for PostgreSQL)
  - django-taggit
  - markdown
- Install dependencies with:

``` bash
pip install django python-decouple psycopg2-binary django-taggit markdown
```

## Installation

1. **Clone the Repository:**
``` bash
git clone https://github.com/Mohammed-Aljazzar/Blog-Application.git
cd Blog-Application
```

2. **Set Up Virtual Environment:**
``` bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**
``` bash
pip install -r requirements.txt
```
4. **Install Docker**
5. **Set Up PostgreSQL with Docker:**
   - Using Docker Command: Run a PostgreSQL container:
   ``` bash
   docker run --name blog-postgres -e POSTGRES_USER=bloguser -e POSTGRES_PASSWORD=blogpass -e 
   POSTGRES_DB=blogdb -p 5432:5432 -d postgres:12
   ```
6. **Configure Environment Variables:**
  - Create a .env file in the project root:
``` bash
DB_NAME=blogdb
DB_USER=bloguser
DB_PASSWORD=blogpass
DB_HOST=localhost
DB_PORT=5432
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL="Your Name <your-email@gmail.com>"
```
Generate an App Password from Google Account Settings if using Gmail SMTP.

7. **Apply Migrations:**
```
python manage.py makemigrations
python manage.py migrate
```

8. **Create a Superuser (for admin access):**
``` bash
python manage.py createsuperuser
```

9. **Run the Server:**
```
python manage.py runserver
```

 - Visit http://127.0.0.1:8000/ in your browser.
 - Access the admin panel at http://127.0.0.1:8000/admin/.

## Usage
### Creating and Managing Posts
 - Log in to the admin panel (/admin/) to create or edit posts.
 - Set the post status to "Published" to make it visible on the blog.
 - Add tags to categorize posts (e.g., "Django", "Python").

### Searching Posts
 - Navigate to /blog/search/ to use the search feature.
 - Enter keywords to find posts by title, with typo-tolerant results (e.g., "yango" finds "Django").
 - Results are displayed in cards with snippets and "Read more" links.

### Commenting
 - On a post’s detail page (/blog/YYYY/MM/DD/slug/), submit comments using the form.
 - Admins can toggle comment visibility in the admin panel.

### Sharing Posts
 - Use the "Share" link on a post’s detail page to send it via email.
 - Fill in the form with your name, email, recipient’s email, and optional comments.

### RSS Feed
 - Subscribe to the RSS feed at /blog/feed/ using an RSS reader.
 - The feed includes the latest 5 published posts.

### Viewing Sitemap
 - Access the sitemap at /sitemap.xml for SEO purposes.
 - It lists all published posts with their last modification dates.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
