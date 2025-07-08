import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    characters = string.ascii_letters  

    if use_digits:
        characters += string.digits  
    if use_special:
        characters += string.punctuation  

    if not characters:
        return "No characters selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔐 Password Generator 🔐")
    
    try:
        length = int(input("Enter password length (default 12): ") or 12)
    except ValueError:
        length = 12

    use_digits = input("Include digits? (y/n, default y): ").lower() != 'n'
    use_special = input("Include special characters? (y/n, default y): ").lower() != 'n'

    generated = generate_password(length, use_digits, use_special)
    print("\nGenerated Password:\n", generated)
