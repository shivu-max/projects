# 🚀 BlogBeam

BlogBeam is a lightweight and fully functional blog web application built using **Flask**.  
It allows users to log in and manage blog posts with complete CRUD (Create, Read, Update, Delete) functionality.

This project demonstrates backend web development fundamentals including routing, authentication, database integration, session management, and template rendering.

---

## 🌟 Overview

BlogBeam is designed as a simple blogging platform where authenticated users can:

- Log in securely
- Create new blog posts
- Edit existing posts
- Delete posts
- View all published posts

The application uses **Flask** as the backend framework and **SQLite** as the database.

---

## ✨ Features

- 🔐 User Authentication (Login / Logout)
- 📝 Create Blog Posts
- ✏️ Edit Existing Posts
- ❌ Delete Posts
- 🗄️ SQLite Database Integration
- 🎨 Dynamic Rendering with Jinja2
- 📦 Clean and Structured Project Architecture

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Database:** SQLite  
- **ORM:** Flask-SQLAlchemy  
- **Templating Engine:** Jinja2  
- **Frontend:** HTML5, CSS3  

---

## 📂 Project Structure

blogbeam/
│
├── blogbeam.py          # Main Flask application
├── requirements.txt     # Project dependencies
├── README.md
├── .gitignore
│
├── templates/           # HTML templates
│   ├── layout.html
│   ├── header.html
│   ├── index.html
│   ├── login.html
│   ├── add_post.html
│   └── dropdown.html
│
└── instance/            # Local configuration (ignored from Git)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/shivu-max/blogbeam.git  
cd blogbeam  

### 2️⃣ Create a Virtual Environment

python -m venv .venv  
source .venv/bin/activate      (macOS / Linux)  
.venv\Scripts\activate         (Windows)  

### 3️⃣ Install Dependencies

pip install -r requirements.txt  

### 4️⃣ Run the Application

python blogbeam.py  

Open your browser and visit:

1. http://127.0.0.1:5000
2. http://192.168.1.3:5001

---

## 🗃️ Database

- Database: SQLite  
- File: `app.db`  
- Automatically created when the application runs  
- Excluded from version control using `.gitignore`  

---

## 🔐 Authentication

- Session-based login system  
- Protected routes for post management  
- Logout functionality  

---

## 🎯 Learning Outcomes

This project demonstrates:

- Flask routing and request handling  
- CRUD operations with a relational database  
- Template rendering using Jinja2  
- User session management  
- Backend application structuring  
- Managing virtual environments  
- Writing production-style project documentation  

---

## 🚀 Future Improvements

- User registration system  
- Password hashing using `werkzeug.security`  
- Comment system  
- Rich text editor for posts  
- REST API endpoints  
- PostgreSQL integration  
- Docker support  
- Cloud deployment (Render / Railway / AWS)  

---

## 📜 License

This project is open-source and available.

---

## 👨‍💻 Author

Developed by Shivaraddi.a.v
Backend Developer | Python & Flask Enthusiast
