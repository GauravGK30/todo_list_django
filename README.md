# ✅ Django To-Do App

A full-stack **To-Do List Web App** built using **Python (Django)**, **MySQL**, **HTML/CSS**, and **JavaScript**. 
This app allows users to **add**, **view**, and **delete** their daily tasks. 
It uses a MySQL database to store the data permanently and Django’s powerful backend to manage logic and routing.

---

## 🚀 Features

- 📝 Add new tasks
- 🗑️ Delete tasks
- 📃 View all tasks
- 💾 Data stored in MySQL database
- 🌐 Simple and clean user interface
- 🔒 Secure with Django CSRF protection and form handling

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, JavaScript (Vanilla)
- **Backend:** Python with Django Framework
- **Database:** MySQL
- **Tools:** VS Code, MySQL Workbench, Git

---

## 📁 Folder Structure 

to_do_project/
├── to_do_app/ # Django app (views, models, urls)
│ ├── migrations/
│ ├── templates/
│ │ └── index.html
│ ├── static/
│ │ └── style.css
│ ├── views.py
│ ├── models.py
│ └── urls.py
│
├── to_do_project/ # Django project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── db.mysql # MySQL database
├── manage.py
└── README.md



---

## 💡 How It Works

1. **User adds a task** via the input form.
2. The task is saved to the **MySQL** database using Django’s ORM.
3. All tasks are fetched and displayed dynamically on the homepage.
4. Clicking the delete button removes the task from the database.

---
