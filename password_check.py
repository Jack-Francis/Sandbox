MIN_LENGTH = 8

print(f"Your password must be at least {MIN_LENGTH} characters long.")
password = input("Enter your password: ")
while len(password) < MIN_LENGTH:
    print("Password is too short.")
    password = input("Enter your password: ")
print("Password accepted!")
for i in range(0, len(password)):
    print("*", end="")
