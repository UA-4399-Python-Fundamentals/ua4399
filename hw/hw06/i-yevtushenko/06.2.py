first_login = False
while not first_login:
    login = input("Login: ")
    if login == "First":
        print(f"Hello {login}!!!")
        first_login = True
    else:
        print("Error")

