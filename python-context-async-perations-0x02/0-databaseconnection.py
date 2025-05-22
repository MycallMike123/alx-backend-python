import sqlite3 # Import the sqlite3 module


#Define a custom context manager class to handle database connections
class DatabaseConnection:
    def __init__(self, db_name):
        # Store the database name
        self.db_name = db_name
        self.conn = None # Hold the connection object once created


    def __enter__(self):
        #Open a connection with the sqlite3 database
        self.conn = sqlite3.connect(self.db_name)
        return self.conn # return the connection object for use


    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()


# Usign the custom context manager to perform a database operation
with DatabaseConnection('users.db') as conn:
    cursor = conn.cursor() # Create cursor object
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(results) # Print the query results to the console
