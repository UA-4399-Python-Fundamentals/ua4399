valid_logins = {"First", "Admin", "User123"}
while True:
    login = input("Enter your login: ")
    if login in valid_logins:
        print("Welcome, user!")
        break
    else:
        print("Error: Incorrect login. Please try again.")
        break
