import sqlite3


# Define a custom context manager to execute a SQL Query
class ExecuteQuery:
    def __init__(self, db_name, query, params()):
        self.db_name = db_name  #Database file name
        self.query = query  # SQL query string
        self.params = params  # Query with parameter (tuple)
        self.conn = None
        self.cursor = None


    def __enter__(self):
        # Open the database connection and create a cursor
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()


        # Execute the query with the provided parameters
        self.cursor.execute(self.query, self.params)


        # Return the fetchef result to the calling context
        return self.cursor.fetchall()


    def __exit__(self, exc_type, exc_value, traceback):
        # Close the connection if it is open
        if self.conn:
            self.conn.close()


# Use the context manager to run the parameterized query
with Execute('users.db', "SELECT * FROM users WHERE age > ?", (25)) as results:
    print(results)
