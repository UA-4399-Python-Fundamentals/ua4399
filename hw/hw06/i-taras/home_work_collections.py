######################################## 1 ########################################

# even_numbers = []
# odd_numbers = []
# else_numbers = []

# for el in range(1, 11):
#     if el % 2 == 0:
#         even_numbers.append(el)
#     elif el % 3 == 0 and el % 2:
#         odd_numbers.append(el)
#     else:
#         else_numbers.append(el)


# print(f"Even numbers divisible by 2: {even_numbers}. \nOdd numbers divisible by 3: {odd_numbers}. \nNumbers not divisible by 2 and 3: {else_numbers}.")


######################################## 2 ########################################

login_name = input("Enter your login: ")

while login_name != 'First':
    print("Incorrect login, please try again.")
    login_name = input("Enter your login: ")

print('Welkom!')
