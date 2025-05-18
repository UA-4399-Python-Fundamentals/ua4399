number = int(input("Number = "))
rez = 1
for i in range(1,number+1):

    rez *= i
print(f"factorial for {number} = {rez}")