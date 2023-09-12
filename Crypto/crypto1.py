# pip install cryptography

from cryptography.fernet import Fernet

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt a string
def encrypt_message(key, message):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Decrypt an encrypted string
def decrypt_message(key, encrypted_message):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

# Example usage
if __name__ == "__main__":
    # Generate a random key (you should save this securely if you need to decrypt later)
    key = generate_key()

    # The message you want to encrypt
    original_message = "This is a secret message."

    # Encrypt the message
    encrypted_message = encrypt_message(key, original_message)
    print("Encrypted Message:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt_message(key, encrypted_message)
    print("Decrypted Message:", decrypted_message)
