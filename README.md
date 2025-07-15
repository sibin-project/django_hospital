# 🏥 Django Hospital Appointment System

A full-stack web application built using **Django** that allows users to view doctors, book appointments, and manage patient records with admin control. Designed to streamline the healthcare experience digitally.

---

## 🚀 Features

- 🔍 Browse list of available doctors
- 📅 Book appointments by selecting date, doctor, and time
- ✅ User-friendly interface for patients and admins
- 🧑‍⚕️ Doctor profile view with specialization
- 🔐 Admin dashboard for managing:
  - Doctors
  - Appointment
  - recent news
---

## 🛠️ Tech Stack

| Layer      | Technology         |
|------------|--------------------|
| Frontend   | HTML5, CSS3, Bootstrap |
| Backend    | Python (Django Framework) |
| Database   | SQLite (default Django DB) |
| Styling    | Bootstrap 5, Google Fonts |

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/sibin-project/django_hospital.git
cd hospital
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
pip install -r requirements.txt
python manage.py runserver
