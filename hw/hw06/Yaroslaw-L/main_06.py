#6.1 determine_numbers
even_num = []
div_by_3_num = []
not_div_2_3 = []
for x in range(1, 10):
        if x % 2 == 0:
              even_num.append(x)
        if x % 3 == 0:
               div_by_3_num.append(x)
        if x % 2 != 0 and x % 3 != 0:
               not_div_2_3.append(x)
print(even_num)
print(div_by_3_num)
print(not_div_2_3)

#06.2 user_login
logins = ["First"]
user = input("Type your login: ")
while user not in logins:
       print("Error: login not in list")
       user = input("Type your login: ")
print(f"Hello, {user}, nice to see you!")