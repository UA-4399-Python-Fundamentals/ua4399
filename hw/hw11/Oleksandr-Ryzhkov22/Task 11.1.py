def your_age(age):
    
    if age % 2 == 0:
        print("Your age is even.")
    else:
        print("Your age is odd.")
    try:
        if age < 0:
            raise ValueError("Age cannot be negative.")
    except ValueError as e:
        print(e)
        
        
def master():
    try:
        age = int(input("Enter your age: "))
        your_age(age)
    except ValueError as e:
        print(f"Please enter a valid number. {e}")
  