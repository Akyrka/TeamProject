# TeamProject

## Authors: Andrii Yermakov and Vova Murai

Django project for electronic diary and forum.

[Usage](#usage)

## Description

* User profile and changing it
* Event notification
* Homework management
* Class schedule
* Forum for communication
* User authentication (teachers and students)

---

## Requirements

* Python 3.11+
* Django 5.2+
* All dependencies listed in `requirements.txt`

---

## Installation and Running

1. **Clone the repository:**

```bash
git clone https://github.com/Akyrka/TeamProject.git
cd TeamProject
```

2. **Create a virtual environment and activate it:**

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Apply migrations:**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser (admin):**

```bash
python manage.py createsuperuser
```

6. **Run the development server:**

```bash
python manage.py runserver
```

7. **Open in your browser:**

```
http://127.0.0.1:8000/
```

---

## Usage

* Teachers can create and edit homework assignments.
* Students can only see their classes and homework.
* Use the Django admin panel to manage users and models:
  `http://127.0.0.1:8000/admin/`

---


