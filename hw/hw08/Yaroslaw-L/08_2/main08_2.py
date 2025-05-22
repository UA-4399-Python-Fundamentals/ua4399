##08.2 check the validity
import re 
logins = r'^(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$'
user = input("Type login for check: ")
def validity(user):
        if re.match(logins, user):
               print("Password is valid!")
               return True
        else: print("Check the input. \n*Must contain letters from a to z, at least one uppercase letter \n*at least one number\n*one symbols $ or # or @ and lenght between 6 and 16.")
validity(user)