import random
x = str(random.randint(1, 499))
y = str(random.randint(500, 999))
print(f"x = {x}, y = {y}")
x, y = y, x
print(f"After swap: x = {x}, y = {y}")
