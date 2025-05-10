fibonacci = [0, 1]
print(fibonacci)
number = int(input("How long must be fibonacci sequence: "))
if number <= 2:
    print (fibonacci[:number])
else:
    while len(fibonacci) != number:
        fibonacci.append(fibonacci[-1]+ fibonacci[-2])
    print(fibonacci)
