# x = 15
# y = 10
# print(x == y)  # False
# print(x != y)  # True
# print(x > y)   # True
# print(x < y)   # False
# print(x >= y)  # True
# print(x <= y)  # False


# a = True
# print(a)  # True
# print(not a)  # False
# print(a == True)  # True 

# a = True
# b = False
# c = True
# print(a and b)  # False
# print(a and c)  # True

# a = 10
# b = 20
# c = 30
# print(a < b and b < c)  # True
# print(a < b and b > c)  # False

# a = "Hello"
# b = "World"
# c = 10
# f1 = 0
# f2 = []
# print(a and b and c)  # 10
# print(a and c and b)  # World
# print(a and c and f1 and f2 and b)  # World
# print(a and c and f2 and f1 and b)  # World

# is_false = [False, 0.0, 0, None, "", [], {}, (),]
# s = " "
# if s:
#     print("True")
# else:  
#     print("False")


# if l:
#     print("True")
# else:
#     print("False")

# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# l3 = l1
# print(l1 == l2)  # True
# print(l1 is l2)  # False
# print(id(l1) == id(l2))  # Memory address of l1 and l2 are different
# print(l1 is l3)  # True
# print(l1 is not l2)  # True


# l = [1, 2, 3, [4, 5, 6], (7, 8, 9), {10, 11, 12}, {13: "hello", 14: "world"}]
# print(f"{1 in l =}")  # True
# print(f"{4 in l =}")  # False
# print(f"{4 not in l =}")  # True
# print(f"{[4, 5, 6] in l =}")  # True
# print(f"{[5, 4, 6] in l =}")  # False
# print(f"{(7, 8, 9) in l[3] =}")  # True
# print(f"{(7, 9, 8) in l[3] =}")  # True
# # print(!True) #SyntaxError: invalid syntax
# print(f"{not True=}")

# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# l3 = [1, 3, 2]
# print(f"{l1 == l2 =}")  # True

# s1 = set("hello")
# s2 = set("lohel")
# print(f"{s1 == s2 =}")  # True

# print(f"{s1 is s2 =}")  # False

# a = 10
# if a == 10:
#     print("\ta is 10")
#     print("\tThis is inside the if block")
# print("This is outside the if block")
# if a > 10:
#     print("\ta > 10")
#     print("\tThis is inside the if block")
# print("This is outside the if block")

# if a > 10: print("\ta > 10")
#     # print("\tThis is inside the if block") ## IndentationError: expected an indented block
# print("This is outside the if block")

# a = 10
# b = 20
# c = 30

# if a < b and b < c:
#     print("\ta < b and b < c")
# print("This is outside the if block")

# if a < b < c:
#     print("\ta < b and b < c")


# temperature = float(input('What is the temperature? '))
# if temperature > 30:
#     print('Wear shorts.')
#     print('Wear a t-shirt.')
# else:
#     print('Wear long pants.')
#     print('Wear a jacket.')
# print('Get some exercise outside.')
      
# age = int(input('Enter your age: '))

# if age < 12:
#     print('You are a kid.')
# else:
#     if age < 18:
#         print('You are a teenager.')
#     else:
#         if age < 65:
#             print('You are an adult.')
#         else:
#             print('You are a senior citizen.')
# print('Have a nice day!')

# if age < 12:
#     print('You are a kid.')
# elif age < 18:
#     print('You are a teenager.')
# elif age < 65:
#     print('You are an adult.')
# else:
#     print('You are a senior citizen.')
# print('Have a nice day!')


# weather = "raining"
# print("Open Your umbrella" if weather == "raining" else "Wear your cap")

# a = 10
# b = 30
# if a > 10:
#     b += 10
# else:
#     b -= 10
# print(b)  # 20

# b += 10 if a > 10 else -10
# print(b)  # 10
# # b += a > 10 ? 10 : -10



# http_status = int(input("Enter HTTP status code: "))
# match http_status:
#     case 200:
#         print("OK")
#     case 201:
#         print("Created")
#     case 204:
#         print("No Content")
#     case 301:
#         print("Moved Permanently")
#     case 400:
#         print("Bad Request")
#     case 401:
#         print("Unauthorized")
#     # case _: #SyntaxError: wildcard makes remaining patterns unreachable
#     #     print("Unknown Status Code")
#     case 403:
#         print("Forbidden")
#     case 404:
#         print("Not Found")
#     case _: 
#         print("Unknown Status Code")

# print("End of program")

# if http_status == 200:
#     print("OK")
# elif http_status == 201:
#     print("Created")
# elif http_status == 204:
#     print("No Content")
# elif http_status == 301:
#     print("Moved Permanently")
# elif http_status == 400:
#     print("Bad Request")
# elif http_status == 401:
#     print("Unauthorized")
# elif http_status == 403:
#     print("Forbidden")
# elif http_status == 404:
#     print("Not Found")
# else:
#     print("Unknown Status Code")
# print("End of program")


# status = int(input("Enter HTTP status code: "))
# match status:
#     case 400:
#         print("Bad request")
#     case 401 | 403 as error:
#         print(f'{error} is authentication error')
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")


# values = input("Enter command: ").split()
# # input_values = ["load", "http://example.com"] #load http://example.com
# # input_values = ["save", "http://example.com", "file1.txt"] # save http://example.com file1.txt
# # input_values = ["save", "http://example.com", "file1.txt", "file2.txt"] # save kukuruku file1.txt file2.txt
# # input_values = ["save", "http://example.com", "file1.txt", "file2.txt", "file3.txt"] # save http://example.com file1.txt file2.txt file3.txt
# # input_values = ["unknown", "http://example.com"] # unknown http://example.com
# match values:
#     case "load", link:
#         print("load", link)
#     case "save", some_value, filename:
#         print(f"saved {some_value} in file {filename}")
#     case "save", link, *filenames:
#         print(f"saved {link} in files: {filenames}")
#         for filename in filenames:
#             print(f"\t{filename}")
#     case _:
#         print(f"Unknown command: {values}")

a = True
b = 0

if a is True:
    print("a is True")
if b:
    print("b is True")

