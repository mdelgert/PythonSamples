from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
import base64

# Generate a random salt (you should save this securely)
salt = b'salt1234'

# Generate a key from the password and salt
def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,  # You can adjust the number of iterations
        salt=salt,
        length=32  # The desired key length in bytes
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

# Encrypt a string with a password
def encrypt_message(password, salt, message):
    key = generate_key(password, salt)
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Decrypt a string with a password
def decrypt_message(password, salt, encrypted_message):
    key = generate_key(password, salt)
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

# Example usage
if __name__ == "__main__":
    # Set your password and message
    password = "password"
    message = "Hello secret message!"

    # Encrypt the message
    encrypted_message = encrypt_message(password, salt, message)
    print("Encrypted Message:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt_message(password, salt, encrypted_message)
    print("Decrypted Message:", decrypted_message)
