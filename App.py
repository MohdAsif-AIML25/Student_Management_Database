# Import necessary modules from Flask
from flask import Flask, request, jsonify, render_template

# Import the database initialization function
from database import init_db

# Import all CRUD functions from models.py
import models

# Create a Flask application instance
app = Flask(__name__)

# Initialize the database (creates tables if they don't exist)
init_db()

# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route("/")
def home():
    # Render the homepage HTML template (index.html)
    return render_template("index.html")
# -----------------------------
# GET ALL STUDENTS
# -----------------------------
@app.route('/students', methods=['GET'])
def get_students():
    # Call the function to retrieve all students from the database
    data = models.get_all_students()
    
    # Return the data as JSON
    return jsonify(data)
# -----------------------------
# ADD STUDENT
# -----------------------------
@app.route('/students', methods=['POST'])
def add_student():
    # Get JSON data sent in the request body
    data = request.get_json()
    # Extract individual fields from the JSON
    name = data.get("Name")
    age = data.get("Age")
    email = data.get("Email")
    contact = data.get("Contact_no")

    # Call the function to insert a new student into the database
    models.add_student(name, age, email, contact)
    # Return a success message with HTTP status 201 (Created)
    return jsonify({"message": "Student added successfully!"}), 201

# -----------------------------
# GET SINGLE STUDENT BY ID
# -----------------------------
@app.route('/students/<int:student_id>', methods=['GET'])
def get_single_student(student_id):
    # Retrieve the student by ID from the database
    student = models.get_student_by_id(student_id)
    if student:
        # Return the student data as JSON
        return jsonify(student)
    # Return error if student not found
    return jsonify({"error": "Student not found"}), 404

# -----------------------------
# UPDATE STUDENT
# -----------------------------
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    # Get JSON data from the request body
    data = request.get_json()

    # Extract updated fields
    name = data.get("Name")
    age = data.get("Age")
    email = data.get("Email")
    contact = data.get("Contact_no")

    # Call the function to update the student in the database
    models.update_student(student_id, name, age, email, contact)
    # Return a success message
    return jsonify({"message": "Student updated successfully!"})

# -----------------------------
# DELETE STUDENT
# -----------------------------
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    # Call the function to delete the student from the database
    models.delete_student(student_id)
    # Return a success message
    return jsonify({"message": "Student deleted successfully!"})
# -----------------------------
# RUN THE FLASK APPLICATION
# -----------------------------
if __name__ == '__main__':
    # Run the app in debug mode for development (auto-reloads on code changes)
    app.run(debug=True)
