''' task 1.2 from HW06'''
# Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is
# different, send an error message.
# (need to use loop while)

# Declaring variables and constant
LOGIN_TRY = "First"

# function to check user login
def check_login():
    while True:
        login_user = input('please enter your login: ')
        if login_user == "First":
            print("Heloo the First")
            break
        else:
            print(f"{login_user} is incorrect, try again")
            

check_login()
