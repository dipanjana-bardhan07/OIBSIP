import random
import string


def generate_password():
    print("=== Welcome to the Oasis Infobyte Password Generator ===")
    

    try:
        # Enforce minimum length of 8
        length = int(input("Enter the desired password length (Minimum 8): "))
        if length < 8:
            print("Error: Password length must be at least 8 characters!")
            return
            

        print("\nChoose character types to include:")
        include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        include_digits = input("Include numbers? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        

        # Character pool generation
        char_pool = ""
        if include_upper:
            char_pool += string.ascii_uppercase
        if include_lower:
            char_pool += string.ascii_lowercase
        if include_digits:
            char_pool += string.digits
        if include_symbols:
            char_pool += string.punctuation
            

        # At least two types check
        selected_types = sum([include_upper, include_lower, include_digits, include_symbols])
        if selected_types < 2:
            print("Error: You must select at least 2 character types for security!")
            return
            

        # Generating password
        password = "".join(random.choice(char_pool) for _ in range(length))
        print(f"\nYour Secure Generated Password is: {password}")
        
        
    except ValueError:
        print("Error: Please enter a valid number for length!")

if __name__ == "__main__":
    generate_password()