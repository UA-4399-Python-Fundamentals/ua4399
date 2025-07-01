def check_age(age):
    try:
        age = int(age)
        1 / (age > 0)
        if age % 2 == 0:
            return f"Age {age} is even"
        else:
            return f"Age {age} is odd"
    except Exception:
        return "Age should be positive number"

age = input()
print(check_age(age))