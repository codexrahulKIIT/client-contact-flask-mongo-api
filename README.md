# 🗂️ Client Contact Management API (Flask + MongoDB)

This project is a simple and customizable REST API built using **Flask** and **MongoDB** that lets you manage client contacts. You can perform all the basic CRUD operations (Create, Read, Update, Delete), and there's also a basic web interface to interact with the backend.

Perfect if you're learning API development, backend integration, or working on a full-stack project using Python and JavaScript!

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![MongoDB](https://img.shields.io/badge/database-MongoDB-green)
![Flask](https://img.shields.io/badge/framework-Flask-lightgrey)

---

## 🧠 Tech Stack

- **Backend:** Flask (Python)
- **Database:** MongoDB using `pymongo`
- **Frontend:** HTML, CSS, JavaScript

---

## 🚀 Features

- Add new client contacts  
- View all existing clients  
- Update client details  
- Delete client records  
- MongoDB integration with `pymongo`  
- Simple HTML + JS frontend  
- API also works with Postman or curl for testing

---

## 📁 Project Structure

```
client-contact-api/
│
├── app.py              # Main Flask app
├── client_routes.py    # API route handlers
├── templates/          # HTML files
│   └── index.html
├── static/             # CSS & JS
│   ├── styles.css
│   └── script.js
├── requirements.txt    # Dependencies
├── .gitignore
└── README.md
```

---

## 📸 Screenshots

### 🖥️ Client Manager Webpage
![Client Manager Webpage](https://github.com/codexrahulKIIT/client-contact-flask-mongo-api/blob/bd808323d6a2d4cca67a6d3c4dd6b97b9fbf8372/screenshot/ClientContactmanger%20webpage%20shot.png?raw=true)

### 📬 Postman Request Example
![Postman Request](https://github.com/codexrahulKIIT/client-contact-flask-mongo-api/blob/bd808323d6a2d4cca67a6d3c4dd6b97b9fbf8372/screenshot/Postman%20%20req.png?raw=true)

---

## 🔧 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/codexrahulKIIT/client-contact-flask-mongo-api.git
cd client-contact-flask-mongo-api
```

### 2️⃣ Set Up a Virtual Environment (Optional)

```bash
# Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

### 4️⃣ Make Sure MongoDB is Running

Make sure MongoDB is running on `localhost:27017`.

You can also use [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) if you prefer a cloud version.

---

### ▶️ Run the Flask Server

```bash
python app.py
```

The server will start here:

```
http://127.0.0.1:5000
```

---

## 🌐 API Endpoints

| Method | Endpoint         | Description         |
|--------|------------------|---------------------|
| GET    | `/clients`       | Get all clients     |
| POST   | `/clients`       | Add a new client    |
| PUT    | `/clients/<id>`  | Update client by ID |
| DELETE | `/clients/<id>`  | Delete client by ID |

---

## 🔽 Sample JSON (POST or PUT)

```json
{
  "name": "Rahul kumar",
  "email": "rahulkumar761001@gmail.com",
  "company": "KIIT",
  "phone": "+91 6202587293",
  "status": "Active"
}
```

---

## ✅ Test Coverage

To make sure the API works properly, I wrote proper unit and integration tests.

- ✔️ Used `pytest`, `coverage.py`, `requests`, and `mongomock` for testing
- ✔️ Wrote tests for all CRUD routes
- ✔️ Tested both valid and invalid input cases
- ✔️ Mocked the database to isolate logic
- ✔️ Achieved **100% test coverage**

📷 **Coverage Report Screenshot**  
![Coverage Report](https://github.com/codexrahulKIIT/client-contact-flask-mongo-api/blob/93d99bfad64c03fcd3e53d27727ffb18d173e77a/screenshot/Coverage%20report.png?raw=true)

---

## 🧪 How to Run the Tests

```bash
# Run the tests
pytest

# Generate test coverage report
coverage run -m pytest
coverage report

# (Optional) Generate HTML report
coverage html
```

Then open `htmlcov/index.html` in your browser to see the report.

---

## 🧪 How to Test the API (Manually)

You can test the API in any of these ways:

✅ **Postman** – Import the endpoints and test them directly  
✅ **curl** – Command line tool to hit your endpoints  
✅ **Web UI** – Just visit: `http://127.0.0.1:5000/`  
It has a clean and simple form to add, update, and delete clients.

> The UI is made using plain HTML, CSS, and JavaScript.

---

## ☁️ Deployment

Currently working on deployment using AWS EC2.

---

## ✍️ Author

**Rahul Kumar**  
GitHub: [@codexrahulKIIT](https://github.com/codexrahulKIIT)
