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
---

## ✅ Keploy API Test Reports

The following screenshots show that Keploy successfully captured and passed all API test cases via the GitHub Actions CI/CD pipeline and Keploy Cloud.

### 📸 Keploy API Test Dashboard

![Keploy API Test Dashboard](https://github.com/codexrahulKIIT/client-contact-flask-mongo-api/blob/fd283495f85d9e344e0c73b05f0ec6b5ddb078af/screenshot/Keploy%20Api%20test%20Dashboard.png?raw=true)

---

### 📋 Captured Test Suites

![Test Suites](https://github.com/codexrahulKIIT/client-contact-flask-mongo-api/blob/fd283495f85d9e344e0c73b05f0ec6b5ddb078af/screenshot/test%20suits.png?raw=true)

---

## 🔁 CI/CD Integration with GitHub Actions

This project uses a GitHub Actions workflow to automatically:

- 🐍 Set up Python & MongoDB
- 🔁 Install dependencies
- ⚙️ Run Keploy API test suite with cloud upload
- ✅ Ensure all test cases pass during every push/pull to `main`

👉 **CI/CD Workflow Execution Link**:  
[View GitHub Actions Runs](https://github.com/codexrahulKIIT/client-contact-flask-mongo-api/actions)

---

### 📝 Summary

- API Test Cases captured & passed with Keploy ✅  
- CI/CD tested & validated on GitHub Actions ✅  
- Dashboard visible on Keploy Cloud ✅  
- Images added for visual proof ✅  


## ✍️ Author

**Rahul Kumar**  
GitHub: [@codexrahulKIIT](https://github.com/codexrahulKIIT)

---

