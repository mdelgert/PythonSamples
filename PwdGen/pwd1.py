import random
import string

def generate_password(length):
    # Define the characters to choose from (letters, digits, and special characters)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password by selecting characters randomly from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Usage example:
password_length = 148  # You can change this to your desired password length
password = generate_password(password_length)
print("Generated Password:", password)
