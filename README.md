# 🗂️ Client Contact Management API (Flask + MongoDB)

This project is a custom RESTful API built with **Flask** and **MongoDB** that allows you to manage client contacts through full CRUD operations (Create, Read, Update, Delete). A simple **web-based frontend** is included to interact with the backend API.

It’s perfect for learning API development, database integration, and full-stack project structure using Python and JavaScript.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![MongoDB](https://img.shields.io/badge/database-MongoDB-green)
![Flask](https://img.shields.io/badge/framework-Flask-lightgrey)

---

## 🧠 Tech Stack

- **Backend:** Flask (Python)
- **Database:** MongoDB (via `pymongo`)
- **Frontend:** HTML, CSS, JavaScript

---

## 🚀 Features

- Add new client contacts  
- View all client records  
- Update existing client details  
- Delete client entries  
- MongoDB integration using `pymongo`  
- Simple HTML + JS frontend for user interaction  
- API testing supported via Postman or curl  

---

## 📁 Project Structure

```
client-contact-api/
│
├── app.py              # Main Flask server
├── client_routes.py    # API route handlers
├── templates/          # HTML files (Frontend)
│   └── index.html
├── static/             # JS, CSS files
│   ├── styles.css
│   └── script.js
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignore unnecessary files
└── README.md           # Project documentation
```

---

## 🖼️ Screenshot

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

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)

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

⚠️ Ensure MongoDB is running on `localhost:27017`.  
You can also use [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) for cloud hosting.

---

### ▶️ Run the Flask Server

```bash
python app.py
```

The server will start on:

```
http://127.0.0.1:5000
```

---

## 🌐 API Endpoints

| Method | Endpoint         | Description         |
|--------|------------------|---------------------|
| GET    | `/clients`       | Fetch all clients   |
| POST   | `/clients`       | Add a new client    |
| PUT    | `/clients/<id>`  | Update client by ID |
| DELETE | `/clients/<id>`  | Delete client by ID |

---

## 🔽 Sample JSON for POST / PUT

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "company": "ABC Corp",
  "phone": "1234567890",
  "status": "Active"
}
```

---

## 🧪 How to Test the API

You can test your API using any of the following:

✅ **Postman**  
Import endpoints and send GET/POST/PUT/DELETE requests.

✅ **curl**  
Example:

```bash
curl http://127.0.0.1:5000/clients
```

✅ **Built-in Frontend**  
Just open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.  
It includes a simple UI to add, update, and delete clients.

> Built with plain HTML, CSS, and JavaScript

---

## ☁️ working on deployment on AWS EC2
---

## ✍️ Author

## ✅ Test Coverage

- Achieved 100% test coverage using `pytest` and `coverage.py`.
- All CRUD routes tested thoroughly with valid and invalid scenarios.
- Integration and API tests verified using `mongomock` and `requests`.

![Coverage Report](screenshots/coverage.png)

**Rahul Kumar**  
GitHub: [@codexrahulKIIT](https://github.com/codexrahulKIIT)

---

