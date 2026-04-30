# Sanguis Blood Management System 🩸

![developer](https://img.shields.io/badge/Developed%20By%20%3A-Arijit%20Mandal-red)
![django](https://img.shields.io/badge/Framework-Django-green)
![tailwindcss](https://img.shields.io/badge/Styling-Tailwind%20CSS-blue)
![status](https://img.shields.io/badge/Status-Active-success)

**Sanguis Blood Management System** is a state-of-the-art, premium 2026 SaaS healthcare application designed to seamlessly bridge the gap between hospitals, blood donors, and patients. Built with a powerful Django backend and a visually stunning, responsive Tailwind CSS frontend interface.

---

## ✨ Key Features

### 🏢 Admin Capabilities
- **Advanced Dashboard Analytics:** Live Chart.js integration showing blood stock distribution (Pie & Bar charts) and dynamic Donation Growth Trends.
- **Strict Role-Based Access Control:** Secure backend routing that isolates Admin panels from unauthorized user access.
- **Inventory Management:** Update, monitor, and manage the exact units available for each blood group (A+, B-, O+, etc.).
- **User Management:** Full CRUD capabilities for Donors and Patients.
- **Request Workflows:** Approve or Reject incoming blood requests and donations with automated inventory calculations.

### ❤️ Donor Experience
- **Premium User Dashboard:** Clean, glassmorphism UI showing dynamic stats (Pending, Approved, Rejected requests).
- **Gamification & Impact Tracker:** Tracks lifetime donations, unlocks achievements/badges, and calculates loyalty points.
- **Live Hospital Demand Analytics:** View real-time, network-wide analytics showing exactly which blood groups are currently in the highest demand.
- **Smart Donation Form:** Integrated pre-donation checklist and modern form UI.
- **Donation Appointments:** Built-in models to schedule future blood donation slots.

### 🏥 Patient Capabilities
- **Effortless Onboarding:** Split-screen React-style registration process with beautiful healthcare illustrations.
- **Emergency Requests:** Request life-saving blood units via an intuitive, icon-rich dashboard form.
- **Real-Time Tracking:** Track pending blood requests and view a complete request history.
- **Responsive Navigation:** Smooth mobile drawer navigation and dark/light mode toggle.

---

## 🎨 Technology Stack

- **Backend:** Python, Django
- **Database:** SQLite (Easily scalable to PostgreSQL)
- **Frontend Framework:** Vanilla HTML/JS powered entirely by **Tailwind CSS**
- **Data Visualization:** Chart.js
- **Icons:** FontAwesome
- **Styling Details:** Global Dark Mode, Glassmorphism Cards, Smooth CSS Micro-animations

---

## 🚀 How To Run This Project Locally

### 1. Prerequisites
- Install **Python (3.9+)** (Don't forget to tick "Add to Path" during installation).
- Install **Git**.

### 2. Clone the Repository
```bash
git clone https://github.com/Arijit065/SANGUIS-Blood-Bank-Management-System.git
cd SANGUIS-Blood-Bank-Management-System
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
*(If `requirements.txt` is missing, ensure you have `django` and `django-widget-tweaks` installed).*

### 4. Database Migrations
Run the following commands to initialize the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an Admin Account
```bash
python manage.py createsuperuser
```
Follow the prompts to set your Admin username, email, and password.

### 6. Start the Server
```bash
python manage.py runserver
```

### 7. Access the Application
Open your preferred web browser and navigate to:
```
http://127.0.0.1:8000/
```

---

## 🔒 Access Portals

- **Patient Portal:** `http://127.0.0.1:8000/patient/patientlogin`
- **Donor Portal:** `http://127.0.0.1:8000/donor/donorlogin`
- **Admin Portal:** `http://127.0.0.1:8000/adminlogin`

---

## 🤝 Feedback & Contributions
Any suggestions and feedback are welcome! Feel free to open an Issue or submit a Pull Request.

*Developed with ❤️ by Arijit Mandal.*
