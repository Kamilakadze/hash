import hashlib


def sha256(input):
    return hashlib.sha256(input.encode()).hexdigest()

choice = input("Enter '1' to sign up or '2' to sign in: ")

if choice == '1':
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("user.txt", "a") as file:
        file.write(f"{username}, {sha256(password)}\n")

    print("Signup successful!")

elif choice == '2':
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("user.txt", "r") as file:
        user_found = False
        for line in file:
            line = line.strip()
            if ", " in line:
                stored_username, stored_password = line.split(", ")
                if stored_username == username:
                    user_found = True
                    if sha256(password) == stored_password:
                        print(f"Welcome, {username}!")
                    else:
                        print("Invalid password!")
                    break

        if not user_found:
            print("User not found!")

else:
    print("Invalid choice!")
