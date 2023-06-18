import random
import string

def generate_password(length=12, use_punctuation=True, use_numbers=True):
    # Define the pool of characters to choose from
    characters = string.ascii_letters
    if use_punctuation:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits

    # Generate a password with random characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Prompt the user for the desired number of passwords
num_passwords = int(input("Enter the number of passwords you want: "))

# Prompt the user for the desired password length
password_length = int(input("Enter the desired password length: "))

# Prompt the user for whether to include punctuation or numbers
use_numbers = input("Do you want to include numbers? (y/n): ").lower() == 'y'
use_punctuation = input("Do you want to include punctuation? (y/n): ").lower() == 'y'

# Generate and print the passwords
passwords = [generate_password(password_length, use_punctuation, use_numbers) for _ in range(num_passwords)]
print("Generated passwords:")
for password in passwords:
    print(password)
