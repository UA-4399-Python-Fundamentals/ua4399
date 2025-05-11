from module_for_task2 import check_password

message = (
    "Password checker program.\n"
    "Password requirements:\n"
    "- 6 to 16 characters\n"
    "- At least 1 lowercase letter\n"
    "- At least 1 uppercase letter\n"
    "- At least 1 number\n"
    "- At least 1 special character: $, #, or @\n"
)

print(message)

while True:
    password = input("Write password (or type 'exit' to quit): ")

    if password.lower() == 'exit':
        print('Bye!')
        break
    if check_password(password):
        print(f"\n\"{password}\" is correct")
        break
    else:
        print(f"\n\"{password}\" is not correct \n")
            
    
