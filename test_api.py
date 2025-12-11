# Import the requests library to make HTTP calls to the Flask API
import requests

# Base URL of the Flask API running locally
BASE_URL = 'http://127.0.0.1:5000'

# List of sample students to add to the database
students = [
    {"Name": "Asif", "Age": 32, "Email": "asif@example.com", "Contact_no": "9876543210"},
    {"Name": "Arif", "Age": 25, "Email": "arif@example.com", "Contact_no": "9892543210"},
    {"Name": "Alice", "Age": 31, "Email": "alice@example.com", "Contact_no": "8876417210"},
    {"Name": "Bob", "Age": 23, "Email": "bob@example.com", "Contact_no": "6876543210"},
    {"Name": "Remo", "Age": 28, "Email": "remo@example.com", "Contact_no": "7976543215"},
    {"Name": "David", "Age": 30, "Email": "david@example.com", "Contact_no": "9876543247"},
    {"Name": "Seenu", "Age": 25, "Email": "seenu@example.com", "Contact_no": "7876543352"},
    {"Name": "Alex", "Age": 22, "Email": "alex@example.com", "Contact_no": "6876567890"}
]

# -----------------------------
# DELETE ALL EXISTING STUDENTS
# -----------------------------
def delete_all_students():
    # Get all existing students from the API
    response = requests.get(f'{BASE_URL}/students')
    
    if response.status_code == 200:
        # Loop through each student and delete by ID
        for student in response.json():
            sid = student[0]   # Index 0 contains Student_id
            requests.delete(f'{BASE_URL}/students/{sid}')
    print("All existing students deleted.")


# -----------------------------
# ADD TEST STUDENTS
# -----------------------------
def add_test_students():
    print("\n--- Adding Students ---")
    for student in students:
        # Send a POST request to add each student
        response = requests.post(f'{BASE_URL}/students', json=student)
        print(response.status_code, response.text)


# -----------------------------
# READ / GET ALL STUDENTS
# -----------------------------
def read_students():
    print("\n--- Reading All Students ---")
    # Send a GET request to fetch all students
    response = requests.get(f'{BASE_URL}/students')
    print(response.json())  # Print the list of student records


# -----------------------------
# UPDATE THE STUDENT WITH ID 2
# -----------------------------
def update_second_student():
    print("\n--- Updating Student ID 2 ---")
    
    updated = {
        "Name": "Ram Kumar",
        "Age": 22,
        "Email": "ram.new@example.com",
        "Contact_no": "9999999999"
    }
    
    # Send a PUT request to update student ID 2
    response = requests.put(f'{BASE_URL}/students/2', json=updated)
    print(response.status_code, response.text)


# -----------------------------
# DELETE THE STUDENT WITH ID 2
# -----------------------------
def delete_second_student():
    print("\n--- Deleting Student ID 2 ---")
    # Send a DELETE request to remove student ID 2
    response = requests.delete(f'{BASE_URL}/students/2')
    print(response.status_code, response.text)


# -----------------------------
# MAIN EXECUTION
# -----------------------------
if __name__ == "__main__":
    delete_all_students()      # Clear database
    add_test_students()        # Add sample students
    read_students()            # Show all students
    update_second_student()    # Update student with ID 2
    read_students()            # Show updated list
    delete_second_student()    # Delete student with ID 2
    read_students()            # Show final list
