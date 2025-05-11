# ________________________exit___ 1 ___________________________

# home_list = [3, 5, 6 ,9, 2]

# new_list = []
# for el in home_list:
#     el = float(el)
#     new_list.append(el)

# print(new_list)


# ___________________________ 2 ___________________________

# n = int(input("Enter number: "))

# first_number = 1
# second_number = 1

# print(first_number, second_number, end=' ')

# while second_number <= n:
#     first_number, second_number = second_number, first_number + second_number
#     print(second_number, end=' ')


# ___________________________ 3 ___________________________

n = int(input("Enter number: "))

x = 1

for el in range(1, n+1):
    x *= el
    print(x, end=' ')
