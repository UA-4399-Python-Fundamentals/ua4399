#TASK 1

# even = []
# odd_div3 = []
# nodiv_2_3 = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         even.append(i)
#     elif i % 3 == 0:
#         odd_div3.append(i)
#     elif i % 2 !=0 and i % 3 !=0:
#         nodiv_2_3.append(i)
# print("Even numbers:", even, "\nOdd numbers that are divisible by 3:", odd_div3, "\nNumbers that are not divisible by 2 and 3:", nodiv_2_3)

#TASK 2

login = input("Login: ")
while login != "First":
    print("Wrong login, try again!")
    login = input("Login: ")
print(f"Greatings, {login}!")