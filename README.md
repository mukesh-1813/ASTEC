# ASTEC Space Club Website

A professional, production-ready Django web application built for the ASTEC Space Club.

## Features
- **Modern UI/UX**: Built with Tailwind CSS, Space Grotesk font, and FontAwesome icons, featuring a sleek, responsive dark space theme.
- **Magazines System**: Browse and read club publications with a built-in PDF viewer.
- **Events System**: View upcoming astronomy events and register online.
- **Custom Admin Portal**: A beautifully branded, lightweight dashboard for club administrators to manage magazines, events, and export registrations to CSV.

## Tech Stack
- **Backend**: Django 5+
- **Database**: SQLite (Development) / PostgreSQL (Production Ready)
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Static files/Media**: WhiteNoise

---

## 🚀 Running the Project Locally

### 1. Prerequisites
- Python 3.10+
- Git

### 2. Setup Instructions

1. **Clone the repository or navigate to the project folder:**
   ```bash
   cd spaceclub
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   
   # Windows:
   .\venv\Scripts\Activate.ps1
   # (Or for cmd: .\venv\Scripts\activate.bat)
   
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r ../requirements.txt 
   # or
   pip install django pillow python-dotenv dj-database-url whitenoise gunicorn
   ```

4. **Set up the Database & Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (Admin Account):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` to see the public site.
   Visit `http://127.0.0.1:8000/admin/` to log into the custom ASTEC dashboard.

---

## 🌍 Deployment Guide (Render)

This project is configured to be easily deployed to [Render.com](https://render.com/).

### 1. Push to GitHub
Commit this project and push it to a GitHub repository.

### 2. Deploy on Render
1. Go to Render.com and create a new **Web Service**.
2. Connect your GitHub repository.
3. Configure the settings:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn config.wsgi:application`
4. Add Environment Variables in Render Dashboard:
   - `SECRET_KEY` = (Generate a long random string)
   - `DEBUG` = `False`
   - `ALLOWED_HOSTS` = `your-render-app-name.onrender.com`
   - `DATABASE_URL` = (Provided by Render when you attach a PostgreSQL database)
5. Click **Create Web Service**.

---

## Directory Structure
```
spaceclub/
│
├── config/        # Project settings, WSGI, ASGI, root URLs.
├── core/          # Static pages (Home, About) and shared templates.
├── magazines/     # Magazine models, views, and templates.
├── events/        # Event management and registrations.
│
├── media/         # Uploaded images and PDFs (ignored in git).
├── static/        # Global static assets (CSS, JS, images).
├── templates/     # Global templates (base layout, admin overrides).
│
├── manage.py
├── .env           # Environment variables (Development).
└── requirements.txt
```
