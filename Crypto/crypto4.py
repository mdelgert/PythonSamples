import hashlib

# Password for encryption and decryption
password = "password"

# Convert the password to bytes
password_bytes = password.encode('utf-8')

# Create an MD5 hash of the password (you can use other hash algorithms)
hash_object = hashlib.md5(password_bytes)
key = hash_object.hexdigest()

# The string you want to encrypt
plaintext = "Hello, this is a secret message."

# Convert the plaintext to bytes
plaintext_bytes = plaintext.encode('utf-8')

# XOR encryption using the hashed key
cipher_text = bytearray()
for i in range(len(plaintext_bytes)):
    cipher_byte = plaintext_bytes[i] ^ ord(key[i % len(key)])
    cipher_text.append(cipher_byte)

# Specify the file name
file_name = "encrypted.txt"

# Save the encrypted text to the specified file
with open(file_name, "wb") as file:
    file.write(cipher_text)

print(f"Encrypted text saved to '{file_name}'")

# To decrypt the text later (using the same key)
with open(file_name, "rb") as file:
    loaded_cipher_text = file.read()

deciphered_text_bytes = bytearray()
for i in range(len(loaded_cipher_text)):
    deciphered_byte = loaded_cipher_text[i] ^ ord(key[i % len(key)])
    deciphered_text_bytes.append(deciphered_byte)

deciphered_text = deciphered_text_bytes.decode('utf-8')

print("Decrypted text:", deciphered_text)
