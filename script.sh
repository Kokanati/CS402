#!/bin/bash

# Function to connect to MySQL and check the password
connect_mysql() {
    mysql -u root -p"$1" -e "SELECT 1;" > /dev/null 2>&1
    if [[ $? -eq 0 ]]; then
        echo "Password found: $1"
        exit 0
    fi
}

# Prompt the user to enter the starting line number
read -p "Enter the line number to start reading from: " start_line

# Validate if the input is a positive integer
if ! [[ "$start_line" =~ ^[0-9]+$ ]] || [[ "$start_line" -le 0 ]]; then
    echo "Please enter a valid positive integer."
    exit 1
fi

# Display a loading message to indicate background execution
echo "Connecting to MySQL... Please wait."

# Read passwords from the file starting from the specified line
total_passwords=$(wc -l < passwords.txt)
current_password=0

# Use tail to skip to the starting line and read from there
tail -n +"$start_line" passwords.txt | while IFS= read -r password; do
    current_password=$((start_line + current_password))
    echo -ne "Testing password $current_password/$total_passwords...\r"
    connect_mysql "$password"
done

# If the loop completes without finding a successful connection, display "password not found"
echo "Password not found."
