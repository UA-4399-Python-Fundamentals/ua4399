#Check the login the user entered
#Greet the user if the login is "First" and send an error if not
def check_login():
    while True:
        user_login = input("Enter your login: ")
        if user_login == "First":
            print("Welcome, First!")
            break
        else:
            print("Error: Invalid login. Please try again.")
check_login()