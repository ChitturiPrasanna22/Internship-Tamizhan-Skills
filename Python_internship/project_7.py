import random
import string
import os

#  Password Generator 
def generate_password(length, use_digits=True, use_special=True):
    if length < 8:
        print("Password length should be at least 8")
        return ""

    # Base characters: letters
    chars = string.ascii_letters

    # Add digits if selected
    if use_digits:
        chars += string.digits

    # Add special characters if selected
    if use_special:
        chars += string.punctuation

    # Ensure password has at least one lowercase, one uppercase, one digit, one special (if included)
    password = []
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    # Fill the remaining length
    while len(password) < length:
        password.append(random.choice(chars))

    # Shuffle for randomness
    random.shuffle(password)

    return "".join(password)

#  Save Password to File 
def save_password(password):
    filename = "passwords.txt"
    with open(filename, "a") as file:
        file.write(password + "\n")
    print(f"Password saved to {filename}")

#  Main Menu 
while True:
    print("\n--- Password Generator Tool ---")
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Enter a valid number")
        continue

    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_special = input("Include special characters? (y/n): ").lower() == "y"

    password = generate_password(length, use_digits, use_special)
    if password:
        print("\nGenerated Password:", password)

        save = input("Save password to file? (y/n): ").lower()
        if save == "y":
            save_password(password)

    cont = input("Generate another password? (y/n): ").lower()
    if cont != "y":
        print("Exiting Password Generator Tool")
        break
