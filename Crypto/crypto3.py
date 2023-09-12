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

# XOR encryption and decryption using the hashed key
cipher_text = bytearray()
for i in range(len(plaintext_bytes)):
    cipher_byte = plaintext_bytes[i] ^ ord(key[i % len(key)])
    cipher_text.append(cipher_byte)

print("Encrypted text:", cipher_text)

# To decrypt the text later (using the same key)
deciphered_text_bytes = bytearray()
for i in range(len(cipher_text)):
    deciphered_byte = cipher_text[i] ^ ord(key[i % len(key)])
    deciphered_text_bytes.append(deciphered_byte)

deciphered_text = deciphered_text_bytes.decode('utf-8')

print("Decrypted text:", deciphered_text)
