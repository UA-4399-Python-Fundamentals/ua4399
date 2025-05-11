# Task 1

def classify_numbers():
    even_div_by_2 = []
    odd_div_by_3 = []
    not_div_by_2_or_3 = []

    for num in range(1, 11):
        if num % 2 == 0:
            even_div_by_2.append(num)
        elif num % 3 == 0:
            odd_div_by_3.append(num)
        if num % 2 != 0 and num % 3 != 0:
            not_div_by_2_or_3.append(num)

    return even_div_by_2, odd_div_by_3, not_div_by_2_or_3

even_div_by_2, odd_div_by_3, not_div_by_2_or_3 = classify_numbers()

print(f"Even numbers divisible by 2: {even_div_by_2}")
print(f"Odd numbers divisible by 3: {odd_div_by_3}")
print(f"Numbers not divisible by 2 or 3: {not_div_by_2_or_3}")


 # Task 2

def check_login():
    while True:
        login = input("Enter your login: ")
        
        if login == "First":
            print("Welcome!")
            break
        else:
            print("Error: Invalid login. Please try again.")

check_login()


