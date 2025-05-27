def even_age(age:int):
    if age < 0:
        raise NegativeNumberError("Age can not be negative")
    if age // 2 == 0:
        return "even" 
    else:
        return "odd"

print(even_age(int(input())))