def password_verification(password):
    if len(password) < 6 or len(password) > 16:
        return False
    
    if not any(char.islower() for char in password):
        return False
    
    if not any(char.isupper() for char in password):
        return False
    
    if not any(char.isdigit() for char in password):
        return False
    
    if not any(char in "$#@" for char in password):
        return False
    
    return True

print("Перевірка валідності пароля")
print("Пароль має містити:")
print("1. Від 6 до 16 символів")
print("2. Принаймні одну малу літеру")
print("3. Принаймні одну велику літеру")
print("4. Принаймні одну цифру")
print("5. Принаймні один спеціальний символ ($#@)")

password = input("Введіть пароль: ")

if password_verification(password):
    print("Пароль валідний")

else:
    print("Пароль не валідний")



    

    