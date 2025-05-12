# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(f"The sum of {a} and {b} is {a + b}")
#     print(a/b)
# except ZeroDivisionError as e:
#     print(f"Error: {e}")
# except ValueError as e:
#     print(f"Error: {e}")


# print("End of program")

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
# except ValueError as e:
#     print(f"Error: {e}")
#     print(f"The sum of {a} and {b} is {a + b}")
# try:
#     print(a/b)
# except :
#     print(f"Error: ")



# print("End of program")
# def read_int():
#     while True:
#         try:
#             a = int(input("Enter a number: "))
#             return a
#         except ValueError as e:
#             print(f"Error: {e}")
#             print("Please enter a valid integer.")

# a = read_int()
# print(f"You entered: {a}")
# print("End of program")



# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
#         # note that braces () are necessary here for multiple exceptions
# # except Exception as e:
# #     print(f"Error: {e}")
# #     print("Please enter a valid integer.")
# # except ArithmeticError:
# #     print("Arithmetic Error!")
# except ValueError as e:
#     print("Value Error!", e)
# # except (NameError, ZeroDivisionError, ) as e:
# #     # print("NameError!", e)
# #     print("NameError! or ZeroDivisionError!", e)
# except:
#     print("Error!")





# def read_int():
#     while True:
#         a = None
#         try:
#             a = int(input("Enter a number: "))
#         except ValueError as e:
#             print(f"Error: {e}")
#             print("Please enter a valid integer.")
#         else:
#             print("No error")
#             return a
#         # finally:
    #         print("Finally block executed")
    #         # This block will always execute
    #         return a*a


# a = read_int()
# print(f"You entered: {a}")
# print("End of program")
# class CustomError(Exception):
#     """Custom exception class."""
#     pass

# def read_str():
#     text = input("Enter a string: ")
#     if not text:
#         # raise ZeroDivisionError("String cannot be empty")
#         raise CustomError("String cannot be empty")
    
#     return text

# s = read_str()
# print(f"You entered: {s}") 

