import random
import string

# Ask the user for password length
length = int(input("Enter the desired password length: "))
# Ask the user for complexity
print("Choose password complexity:")
print("1. Only Letters")
print("2. Letters and Numbers")
print("3. Letters, Numbers, and Special Characters")

choice = int(input("Enter your choice (1/2/3): "))

# Define character sets based on user choice
if choice == 1:
    characters = string.ascii_letters
elif choice == 2:
    characters = string.ascii_letters + string.digits
elif choice == 3:
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice!")
    exit()

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display generated password
print("Generated Password:", password)
