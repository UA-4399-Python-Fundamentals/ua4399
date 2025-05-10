def biggest_number(a,b):
    """This function return biggest number"""
    if a >= b:
        return a
    else:
        return b

print(biggest_number.__doc__)
a = int(input("First number =  "))
b = int(input("First number =  "))

print(f"Bigest number is {biggest_number(a,b)}")
