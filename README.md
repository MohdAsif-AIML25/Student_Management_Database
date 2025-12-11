🚀 Student Management Database API

A complete Student Management System Backend built using Python, Flask, SQLite, and REST APIs, demonstrating CRUD operations, database modeling, and API-driven design.

📘 Project Overview

The Student Management Database API is a backend web service that manages student information using a clean and modular architecture.
It provides REST API endpoints for:

Creating student records

Reading all students

Updating student data

Deleting student records

This project is ideal for learning Flask APIs, database operations, requests module, and Python backend development.

🧠 Aim of the Project

To build a RESTful API-based backend system capable of performing CRUD operations for student data, useful for educational institutions and application developers.

🎯 Goals & Objectives
✔ Goals

Build a REST API using Flask

Store data using SQLite

Implement CRUD operations through API endpoints

✔ Objectives

Create database tables for Students, Courses, and Enrollments

Write modular Python code: app.py, models.py, database.py

Test API endpoints using Python's requests module

Prevent duplicate email entries using validation

🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Flask (2.3.2)	Framework for building the API backend
SQLite	Lightweight database system
SQL	For CRUD operations
Requests	To test API endpoints
JSON	Data exchange format
📁 Project Structure
Student_Management_Database/
│
├── app.py               # Flask API with all routes
├── models.py            # CRUD operations for students
├── database.py          # Database initialization & connection
├── client.py            # Script to test the API with requests
└── README.md            # Project documentation

🚀 API Endpoints
1️⃣ Get All Students

GET /students
Returns all student records.

2️⃣ Add a New Student

POST /students
JSON Body:

{
  "Name": "Alex",
  "Age": 25,
  "Email": "alex@example.com",
  "Contact_no": "9876543210"
}

3️⃣ Update Student Details

PUT /students/<student_id>
JSON Body:

{
  "Name": "John",
  "Age": 22,
  "Email": "john@example.com",
  "Contact_no": "9999999999"
}

4️⃣ Delete Student

DELETE /students/<student_id>

🗄️ Database Schema
students table
Column	Type	Description
Student_id	INTEGER (PK)	Auto-increment primary key
Name	TEXT	Student name
Age	INT	Student age
Email	TEXT UNIQUE	Unique email
Contact_No	TEXT	Phone number
courses table
Column	Type	Description
Course_id	INTEGER (PK)	Auto-increment
Name	TEXT	Course name
Description	TEXT	Details of course
Enrollment table
Column	Type	Description
enrollment_id	INTEGER (PK)	
Student_id	INTEGER (FK)	
Course_id	INTEGER (FK)	
🧪 Testing Using client.py

The client.py script demonstrates:

Adding multiple students

Updating a student

Deleting a student

Deleting all students

Reading all students

Example:

response = requests.post("http://127.0.0.1:5000/students", json=student)
print(response.json())

📌 Why Use This Project?

Easy to integrate with any frontend (React, Flutter, Android, etc.)

Demonstrates clean API design

Great for learning Flask + SQL

Modular and beginner-friendly code structure

Perfect for college projects and real-world practice

📌 When to Use This Project?

Use this project when you need:

A backend for a student management system

A learning reference for APIs and CRUD

A lightweight database-driven application

A backend that frontend apps can consume

⚙️ How to Run the Project
1. Clone the repository
git clone https://github.com/MohdAsif-AIML25/Student_Management_Database.git

2. Install dependencies
pip install flask requests

3. Start the API server
python app.py

4. Run the client test script
python client.py

🤝 Contributions

Contributions are welcome!
Feel free to fork the repo, create a branch, make changes, and submit a pull request.

📜 License

This project is open-source and free to use.
