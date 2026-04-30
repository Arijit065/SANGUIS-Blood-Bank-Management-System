# 🩸 Sanguis Blood Management System

<div align="center">

![developer](https://img.shields.io/badge/Developed%20By-Arijit%20Mandal-red?style=for-the-badge)
![django](https://img.shields.io/badge/Django-3.0.5-green?style=for-the-badge&logo=django)
![python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![tailwindcss](https://img.shields.io/badge/Tailwind%20CSS-UI-38bdf8?style=for-the-badge&logo=tailwindcss)
![license](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**Sanguis Blood Management System** is a premium 2026 SaaS-style healthcare application that bridges the gap between hospitals, blood donors, and patients — built on a Django backend with a fully modern, responsive Tailwind CSS interface.

[🚀 Live Demo](#-how-to-run-this-project-locally) · [📂 GitHub Repo](https://github.com/Arijit065/SANGUIS-Blood-Bank-Management-System) · [🐛 Report a Bug](https://github.com/Arijit065/SANGUIS-Blood-Bank-Management-System/issues)

</div>

---

## 📁 Project Structure

```
SANGUIS-Blood-Bank-Management-System/
│
├── sanguis/                  ← Core Django configuration package
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── blood/                    ← Admin logic & models (Stock, BloodRequest, Notifications)
├── donor/                    ← Donor app (Donations, Requests, Loyalty)
├── patient/                  ← Patient app (Blood Requests, History)
│
├── templates/
│   ├── blood/                ← Admin HTML templates
│   ├── donor/                ← Donor HTML templates
│   └── patient/              ← Patient HTML templates
│
├── static/                   ← CSS, JS, and image assets
├── manage.py
├── requirements.txt
└── README.md
```

---

## ✨ Key Features

### 🏢 Admin Panel
- **Advanced Analytics Dashboard:** Live Chart.js charts — Blood Stock Pie/Bar charts and real-time Donation Growth Trend Line chart.
- **Role-Based Access Control:** Strict, secure routing via Django decorators (`@user_passes_test`) — each role is completely isolated.
- **Full Inventory Management:** Monitor and update blood unit counts for every blood group (A+, A-, B+, B-, AB+, AB-, O+, O-).
- **User Management:** View, Update, and Delete Donors and Patients.
- **Request Approval Workflow:** Approve or Reject blood donation requests and blood unit requests with automated stock recalculation.
- **History Tracking:** Permanent archive of all request decisions.

### ❤️ Donor Experience
- **Premium Glassmorphism Dashboard:** Real-time stat cards (Total, Pending, Approved, Rejected).
- **Live Hospital Demand Chart:** Dynamic bar chart showing which blood groups are most in-demand network-wide.
- **Gamification System:** Loyalty points, donation streaks, and achievement badges (database-ready).
- **Appointment Booking:** Database model to schedule future blood donation slots.
- **Donation History:** Full timeline of past donations with status badges.
- **Smart Blood Request Form:** Submit emergency/standard blood requests with a built-in priority alert.

### 🏥 Patient Experience
- **React-Style Split-Screen Registration:** Professional onboarding with healthcare illustrations.
- **Blood Request Form:** Request specific blood groups and units with a single, elegant form.
- **Request History Table:** Full tracking of all requests with live color-coded status badges (Pending / Approved / Rejected).
- **Dark Mode Support:** Global dark/light mode toggle saved to `localStorage`.

---

## 🎨 Technology Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.9+, Django 3.0.5 |
| **Database** | SQLite (upgradeable to PostgreSQL) |
| **Frontend** | HTML5, Vanilla JS, Tailwind CSS |
| **Charts** | Chart.js |
| **Icons** | FontAwesome 6 |
| **Form Widgets** | django-widget-tweaks |
| **UI Style** | Glassmorphism, Dark Mode, CSS Micro-animations |

---

## 🚀 How To Run This Project Locally

### Step 1: Prerequisites
- Install **Python (3.9+)** — tick **"Add to PATH"** during installation.
- Install **Git**.

### Step 2: Clone the Repository
```bash
git clone https://github.com/Arijit065/SANGUIS-Blood-Bank-Management-System.git
cd SANGUIS-Blood-Bank-Management-System
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

### Step 6: Run the Development Server
```bash
python manage.py runserver
```

### Step 7: Open in Browser
```
http://127.0.0.1:8000/
```

---

## 🔒 Portal Login URLs

| Role | URL |
|---|---|
| 🏠 **Home** | `http://127.0.0.1:8000/` |
| 🏢 **Admin Login** | `http://127.0.0.1:8000/adminlogin` |
| ❤️ **Donor Login** | `http://127.0.0.1:8000/donor/donorlogin` |
| 🏥 **Patient Login** | `http://127.0.0.1:8000/patient/patientlogin` |
| ❤️ **Donor Register** | `http://127.0.0.1:8000/donor/donorsignup` |
| 🏥 **Patient Register** | `http://127.0.0.1:8000/patient/patientsignup` |

---

## 📦 Dependencies (`requirements.txt`)

```
asgiref==3.2.7
Django==3.0.5
django-widget-tweaks==1.4.8
pytz==2020.1
sqlparse==0.3.1
```

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

© 2026 **Arijit Mandal**

---

## 🤝 Feedback & Contributions

All suggestions and feedback are warmly welcome!
Feel free to **open an Issue** or **submit a Pull Request** on GitHub.

<div align="center">

*Developed with ❤️ by **Arijit Mandal***

[![GitHub](https://img.shields.io/badge/GitHub-Arijit065-black?style=flat&logo=github)](https://github.com/Arijit065)

</div>
