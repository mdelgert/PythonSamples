import random
import string

def generate_password(length):
    # Define the character sequences
    sequences = [
        string.ascii_letters,  # Letters (both lowercase and uppercase)
        string.digits,        # Digits (0-9)
        string.punctuation,   # Punctuation symbols
        "¤¶§",                # Additional special characters
        "ÇüéâäàåçêëèïîìæÆôöòûùÿ¢£¥PƒáíóúñÑ¿¬½¼¡«»¦ßµ±°•·²€„…†‡ˆ‰Š‹Œ‘’“”–—˜™š›œŸ¨©®¯³´¸¹¾ÀÁÂÃÄÅÈÉÊËÌÍÎÏÐÒÓÔÕÖ×ØÙÚÛÜÝÞãðõ÷øüýþ"  # Additional special characters
    ]

    # Combine all the character sequences into one
    all_characters = ''.join(sequences)

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Example: Generate a password of length 12
password = generate_password(148)
print(password)
