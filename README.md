# 🔗 URL Shortener | Flask Web Application

> **A lightweight and responsive URL shortening application built with Flask that transforms long URLs into compact, shareable links while demonstrating full-stack web development concepts.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![HTML5](https://img.shields.io/badge/HTML5-Markup-E34F26?logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?logo=javascript)

---

## 📖 Project Overview

Long URLs can be difficult to share, manage, and remember. URL shortening services solve this problem by generating concise, unique links that redirect users to the original destination.

This project implements a **URL Shortener Web Application** using **Flask**, allowing users to create short URLs, store them in a database, and seamlessly redirect users to the original web pages.

The application demonstrates backend development, database integration, routing, and responsive web design.

---

## 🎯 Project Objectives

* Build a complete Flask-based web application
* Generate unique short URLs for long links
* Store URL mappings efficiently in a database
* Implement automatic URL redirection
* Create a clean and responsive user interface
* Demonstrate full-stack development using Python

---

## ✨ Key Features

### URL Shortening

* Convert lengthy URLs into short, easy-to-share links
* Generate unique identifiers automatically
* Fast and lightweight processing

### URL Redirection

* Redirect users to the original destination instantly
* Preserve the original URL without modification
* Reliable routing using Flask

### Database Integration

* Store URL mappings securely
* Efficient data retrieval using SQLAlchemy ORM
* Easy database scalability

### User Experience

* Responsive interface for desktop and mobile devices
* Simple and intuitive workflow
* Graceful handling of invalid URLs and errors

---

## 🏗️ Application Workflow

```text
User Enters URL
        │
        ▼
 Flask Application
        │
        ▼
Generate Unique Short Code
        │
        ▼
Store URL in Database
        │
        ▼
Return Short URL
        │
        ▼
User Opens Short Link
        │
        ▼
Redirect to Original URL
```

---

## 🛠️ Technology Stack

| Category             | Technologies          |
| -------------------- | --------------------- |
| Programming Language | Python                |
| Backend Framework    | Flask                 |
| Frontend             | HTML, CSS, JavaScript |
| Database             | SQLite / MySQL        |
| ORM                  | SQLAlchemy            |
| Version Control      | Git & GitHub          |

---

## 📂 Project Structure

```text
URL-Shortener/
│
├── app.py                 # Flask application
├── models.py              # Database models
├── templates/             # HTML templates
├── static/                # CSS, JavaScript & images
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/pranjalsalvi/url-shortener.git

cd url-shortener
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open in Your Browser

```text
http://127.0.0.1:5000
```

---

## 📌 How It Works

1. Enter a long URL.
2. Click the **Shorten URL** button.
3. The application generates a unique short code.
4. The URL mapping is stored in the database.
5. A shortened URL is returned.
6. Opening the shortened link redirects to the original website.

---

## 💡 Key Highlights

* Flask-based backend architecture
* Database integration with SQLAlchemy
* Automatic URL redirection
* Responsive web interface
* Modular project structure
* Beginner-friendly full-stack project

---

## 📌 Future Enhancements

* User authentication and personalized dashboards
* Custom short URLs
* QR code generation
* Link expiration support
* Click analytics and traffic insights
* Password-protected links
* REST API for URL shortening
* Docker deployment
* Cloud deployment using Render or Railway

---

## 👨‍💻 About Me

**Pranjal Salvi**

Aspiring **Data Analyst & Python Developer** passionate about building practical web applications, data-driven solutions, and AI-powered systems.

### Connect with me

* 🔗 LinkedIn: https://www.linkedin.com/in/pranjal-salvi-380732227/
* 💻 GitHub: https://github.com/pranjalsalvi

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub. Your support motivates me to build and share more open-source projects.

---

### Thank you for visiting this repository! 🚀
