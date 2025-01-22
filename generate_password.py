import itertools
import sys
import time

# Function to generate all possible combinations of the words and write them to a file
def generate_combinations(words, output_file):
    # Load existing words into a set to check for duplicates
    try:
        with open(output_file, 'r') as f:
            existing_words = set(line.strip() for line in f)
    except FileNotFoundError:
        existing_words = set()
    print("Passwords currently generated:")
    with open(output_file, 'a') as f:  # Open in append mode
        for r in range(1, len(words) + 1):
            for combo in itertools.permutations(words, r):
                combination = ''.join(combo)
                
                 # Skip if the combination doesn't meet the length requirement
                if not (4 <= len(combination) <= 20):
                    continue

                # Skip if the combination already exists
                if combination in existing_words:
                    continue  

                existing_words.add(combination)  # Add the new combination to the set
                
                # Display the current word, replacing the previous one
                sys.stdout.write('\r' + " " * 40 + '\r')  # Clear the previous word
                sys.stdout.write(combination)
                sys.stdout.flush()
                
                f.write(combination + '\n')  # Write to file
                time.sleep(0.1)  # Optional: adds a slight delay for visibility

    sys.stdout.write('\r' + " " * 40 + '\r')  # Clear the final word
    sys.stdout.flush()

# Function to read words from a text file and generate new words
def generate_new_words_from_file(input_file, output_file):
    with open(input_file, 'r') as file:
        words = [line.strip() for line in file.readlines()]
    
    generate_combinations(words, output_file)

# Example usage
input_file = 'keywords.txt'  # Replace with your input text file name
output_file = 'passwords.txt'  # Output file name
generate_new_words_from_file(input_file, output_file)

print("\nAll combinations generated and written to", output_file)
