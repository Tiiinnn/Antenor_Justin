import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    while True:
        choice = input("Do you want to generate a strong password? (y/n): ")
        if choice.lower() == 'y':
            password_length = random.randint(8, 12)
            password = generate_password(password_length)
            print(f"Your strong password is: {password}")
        elif choice.lower() == 'n':
            print("No problem! Have a nice day.")
            break
        else:
            print("Invalid input! Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
