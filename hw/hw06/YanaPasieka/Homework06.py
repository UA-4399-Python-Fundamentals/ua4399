#1
for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} - парне")
    elif num % 2 != 0 and num % 3 == 0:
        print(f"{num} - непарне")
    else:
        print(f"{num} —- не ділиться 2 і 3")

#2
login = input()
while login != "First":
    print("Wrong login")
    login = input()
else:
    print("Correct login")