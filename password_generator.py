import random
import string

def generate_password(length=12):
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password with random characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Prompt the user for the desired number of passwords
num_passwords = int(input("Enter the number of passwords you want: "))

# Prompt the user for the desired password length
password_length = int(input("Enter the desired password length: "))

# Generate and print the passwords
passwords = [generate_password(password_length) for _ in range(num_passwords)]
print("Generated passwords:")
for password in passwords:
    print(password)