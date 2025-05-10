def login ():
    login = input("Enter your login: ")
    while login != "First":
        print ("Invalid login")
        break
    if login == "First":
        print("Hello, First!")
            