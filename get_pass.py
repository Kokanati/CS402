import itertools
import sys
import time

# Function to generate all possible combinations of the words and write them to a file
def generate_combinations(words, output_file):
    with open(output_file, 'w') as f:
        print("Passwords currently generated:")
        for r in range(1, len(words) + 1):
            for combo in itertools.permutations(words, r):
                combination = ''.join(combo)
                sys.stdout.write('\r' + " " * 40 + '\r')  # Clear the current password line
                print(combination)  # Print current word on the next line
                f.write(combination + '\n')  # Write to file
                time.sleep(0.1)  # Optional: adds a slight delay for visibility

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
