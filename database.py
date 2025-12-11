import sqlite3

# Name of the SQLite database file
DB_NAME = "students.db"

def get_connection():
    # Connect to the SQLite database file
    # If the file doesn't exist, SQLite will create it automatically
    return sqlite3.connect(DB_NAME)

def init_db():
    # Get a connection to the database
    conn = get_connection()
    
    # Create a cursor object
    # A cursor is used to execute SQL commands (CREATE, SELECT, INSERT, etc.)
    cur = conn.cursor()

    # Execute an SQL command to create a table if it does not already exist.
# Triple quotes allow writing multi-line SQL statements.
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students(
            Student_id INTEGER PRIMARY KEY AUTOINCREMENT,  
            Name TEXT, 
            Age INTEGER, 
            Email TEXT  UNIQUE,
            Contact_No TEXT  
        )
    """)

# Save (commit) the changes to the database
    conn.commit()

# Close the connection to free resources
    conn.close()
