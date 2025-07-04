
# 📁 Employee Management System Backend (Django REST Framework)

## 🚀 Purpose

This project is a **learning-focused backend API** for managing company employees, departments, and HR authentication using **Django** and **Django REST Framework**.

The goal is to:
- Learn Django's structure (models, views, serializers, routing)
- Use JWT-based authentication with `SimpleJWT`
- Practice RESTful API development with SOLID principles

## 🧠 Technologies Used

| Tool | Purpose |
|------|---------|
| Django | Python web framework |
| Django REST Framework | API building |
| SimpleJWT (`djangorestframework-simplejwt`) | JWT authentication (login/refresh tokens) |
| SQLite (default) | Lightweight development database |

## 📂 Folder Structure

```
employee_MS/
├── employee_MS/             # Project settings
│   └── urls.py              # Main routing file
├── employee_app/               # App for HR, Employee, Department logic
│   ├── models.py            # Employee, Department, HR models
│   ├── serializers.py       # DRF serializers for all models
│   ├── urls.py              # API route definitions
│   ├── views/               # Separated view logic
│   │   ├── employee_views.py
│   │   ├── department_views.py
│   │   └── hr_views.py
│   └── permissions.py       # Custom HR-only permission
├── manage.py
└── README.md                
```

## 🔐 Authentication

- **JWT (access & refresh token) based**
- Only users with an HR profile can log in
- Protected endpoints require valid `access` token in the request headers:
  ```
  Authorization: Bearer <access_token>
  ```

## 🔗 API Routes

| Method | URL | Description |
|--------|-----|-------------|
| `GET` | `/api/employees/` | List all employees |
| `POST` | `/api/employee/create/` | Create new employee |
| `PATCH` / `PUT` | `/api/employee/<id>/update/` | Update employee details |
| `DELETE` | `/api/employee/<pk>/delete/` | Delete an employee |
| `POST` | `/api/departments/` | Create a department |
| `PATCH` / `PUT` | `/api/department/<pk>/update/` | Update a department |
| `DELETE` | `/api/department/<pk>/delete/` | Delete a department |
| `POST` | `/api/hr-register/` | Register a new HR user (creates a `User` + `HR`) |
| `POST` | `/api/hr-login/` | Login for HRs (returns `access` and `refresh` tokens) |
| `POST` | `/api/token/refresh/` | Refresh access token using refresh token |

## 🧪 Example JWT Login Flow

1. Login via `/api/hr-login/`  
   Response:
   ```json
   {
     "access": "...",
     "refresh": "...",
     "username": "hr1",
     "department": "Finance"
   }
   ```

2. Use access token in all protected API requests:
   ```
   Authorization: Bearer <access_token>
   ```

3. When access token expires, call:
   ```
   POST /api/token/refresh/
   { "refresh": "<refresh_token>" }
   ```




## 🛠️ Getting Started (Development)

```bash
# Install dependencies
pip install -r requirements.txt

# Make migrations and run server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 👨‍💻 Future Ideas (for practice)

- Add pagination to the employee list
- Add filtering by department
- Add audit logs for updates and deletions
- Implement logout and token blacklisting
- Split frontend (React, Flutter) to consume this API
