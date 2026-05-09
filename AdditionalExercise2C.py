# Setup
correct_password = "ben10THousand"  # Replace with your chosen password
attempts = 0

# Logic
while True:
    user_input = input("Enter password: ")
    attempts += 1
    if user_input == correct_password:
        print("Access Granted!")
        break
    else:
        print("Incorrect, try again.")

# Output
print("Correct Password Set:", correct_password)
print("Attempts Before Success:", attempts)
