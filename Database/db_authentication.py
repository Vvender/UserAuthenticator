import pyodbc


class UserDatabase:
    def __init__(self):
        # Initialize connection and cursor as None
        self.connection = None
        self.cursor = None
        # Establish a database connection
        self.check_initial_setup()

    def db_connect(self, database='UserAuthentication'):
        try:
            # Connect to the SQL Server with autocommit mode enabled
            # Do not forget to change Server name according to your server name
            self.connection = pyodbc.connect(
                'Driver={SQL Server};'
                'Server=DESKTOP-FNO1431\SQLEXPRESS;'
                f'Database={database};'  # Connect directly to the UserAuthentication database
                'Trusted_connection=yes;',
                autocommit=True  # Set autocommit to True to prevent multi-statement transactions
            )
            self.cursor = self.connection.cursor()

        except Exception as e:
            print(f"Error connecting to the database: {str(e)}")
            self.close_connection()

    def close_connection(self):
        try:
            # Close the database connection and cursor
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except Exception as e:
            print(f"Error closing connection: {str(e)}")

    def check_initial_setup(self):
        try:
            self.db_connect('master')
            # Check if the UserAuthentication database exists
            self.cursor.execute("SELECT COUNT(*) FROM sys.databases WHERE name = 'UserAuthentication'")
            if self.cursor.fetchone()[0] == 0:
                # UserAuthentication database does not exist, create it
                print("Database does not exist; initiating setup process")
                self.create_initial_setup()
            else:
                print("Database already exists; no further action is necessary.")

        except Exception as e:
            print(f"Error checking initial setup: {str(e)}")

    def create_initial_setup(self):
        try:
            self.db_connect('master')
            # Create the UserAuthentication database if it does not exist
            self.cursor.execute(
                "IF NOT EXISTS (SELECT 1 FROM sys.databases WHERE name = 'UserAuthentication') CREATE DATABASE UserAuthentication")
            print("UserAuthentication database created.")

            # Use the newly created database
            self.cursor.execute("USE UserAuthentication")

            # Create the users table if it does not exist
            self.cursor.execute("""
                IF NOT EXISTS (SELECT 1 FROM sys.tables WHERE name = 'users') 
                CREATE TABLE users (
                    user_id INT IDENTITY(1,1) PRIMARY KEY,
                    user_name VARCHAR(25) NOT NULL,
                    user_password VARCHAR(25) NOT NULL,
                    phone VARCHAR(25) NOT NULL,
                    email VARCHAR(100) NOT NULL
                )
            """)
            print("users table created.")

            # Insert the initial admin user if not exists
            try:
                self.cursor.execute("""
                    IF NOT EXISTS (SELECT 1 FROM users WHERE user_name = 'admin') 
                    INSERT INTO users (user_name, user_password, phone, email)
                    VALUES ('admin', '12345', '123-456-7890', 'admin@example.com')
                """)
                print("Initial admin user inserted.")
            except Exception as e:
                # Handle the exception for duplicate key
                print(f"Initial admin user already exists: {str(e)}")

            # Commit the changes to persist them
            self.connection.commit()

        except Exception as e:
            print(f"Error creating initial setup: {str(e)}")
        finally:
            self.close_connection()

    def authenticate_user(self, username, password):
        try:
            self.db_connect()
            try:
                # Check if the user credentials are valid
                self.cursor.execute(
                    "SELECT COUNT(*) FROM users WHERE user_name = ? AND user_password = ?", (username, password))
                if self.cursor.fetchone()[0] == 1:
                    print("Access granted")
                    return True
                else:
                    print("Access denied")
                    return False

            except Exception as e:
                print(f"Error during cursor operation: {str(e)}")

        except Exception as e:
            print(f"Error authenticating user: {str(e)}")

    def add_user(self, username, user_password, phone, email):
        try:
            # Check for empty and non-null inputs
            if any(not value or value.isspace() for value in (username, user_password, phone, email)):
                return 1  # Return 1 for empty or whitespace input error

            # Connect to the UserAuthentication database
            self.db_connect()

            # Check for existing records
            query = "SELECT COUNT(*) FROM users WHERE user_name = ? OR phone = ? OR email = ?"
            self.cursor.execute(query, (username, phone, email))
            result = self.cursor.fetchone()

            # Check if the count of matching records is greater than 0
            if result[0] > 0:
                print(f"Checking for duplicates - username: {username}, phone: {phone}, email: {email}")
                print(f"Count of matching records: {result[0]}")
                return 2  # Return 2 for duplicate record error

            # Insert the new user
            query = "INSERT INTO users (user_name, user_password, phone, email) VALUES (?, ?, ?, ?)"
            self.cursor.execute(query, (username, user_password, phone, email))
            self.connection.commit()
            return 0  # Return 0 for successful insertion

        except Exception as e:
            print(f"Error adding user: {str(e)}")
            return 3  # Return 3 for general error

        finally:
            self.close_connection()


# Create an instance of the Library class to trigger the initial setup
user_db = UserDatabase()
