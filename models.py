# import 'get_connections from 'database' file name!...
# This allows us to connect to the SQLite database using get_connection()
from database import get_connection

# Function to add a new student to the 'students' table
def add_student(name, age, email, contact):
    conn = get_connection()
    cur = conn.cursor()
    
    # Execute an SQL INSERT command to add a new student
    # The question marks (?) are placeholders to safely insert values-This prevents SQL injection attacks
    cur.execute(
        "INSERT INTO students (Name, Age, Email, Contact_No) VALUES (?, ?, ?, ?)",(name, age, email, contact))  # Tuple of values to insert
    
    # Save (commit) the changes to the database
    conn.commit()
    
    # Close the connection to free up resources
    conn.close()


# Function to retrieve all students from the 'students' table
def get_all_students():
   
    conn = get_connection()
    cur = conn.cursor()
    
    # Execute an SQL SELECT command to get all records from the 'students' table
    cur.execute("SELECT * FROM students")
    
    # Fetch all rows returned by the SELECT query
    # Each row is a tuple containing (Student_id, Name, Age, Email, Contact_No)
    rows = cur.fetchall()

    conn.close()
    
    # Return the list of tuples containing all student records
    return rows

# -----------------------------
# READ ONE STUDENT BY ID
# -----------------------------
def get_student_by_id(student_id):
    # Get a connection to the database
    conn = get_connection()
    
    # Create a cursor object to execute SQL commands
    cur = conn.cursor()
    
    # Execute a SELECT query to get a student with a specific ID
    # The question mark (?) is a placeholder to safely insert the value
    cur.execute("SELECT * FROM students WHERE Student_id = ?", (student_id,))
    
    # Fetch the first row returned by the query
    # Returns a tuple like (Student_id, Name, Age, Email, Contact_No) or None if not found
    row = cur.fetchone()
    
    # Close the connection to free resources
    conn.close()
    
    # Return the student record
    return row

# -----------------------------
# UPDATE STUDENT
# -----------------------------
def update_student(student_id, name, age, email, contact):
  
    conn = get_connection()

    cur = conn.cursor()
    
    # Execute an UPDATE query to modify the student record with the given ID
    # Question marks (?) are placeholders for the values to safely prevent SQL injection
    cur.execute("""
        UPDATE students
        SET Name=?, Age=?, Email=?, Contact_No=?
        WHERE Student_id=?
    """, (name, age, email, contact, student_id))
    
    conn.commit()
    conn.close()

# -----------------------------
# DELETE STUDENT
# -----------------------------
def delete_student(student_id):
   
    conn = get_connection()
    cur = conn.cursor()
    
    # Execute a DELETE query to remove the student with the specified ID
    cur.execute("DELETE FROM students WHERE Student_id = ?", (student_id,))
    
    conn.commit()
    conn.close()

