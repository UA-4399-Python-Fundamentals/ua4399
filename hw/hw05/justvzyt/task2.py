n = int(input("Enter n: "))

if n < 0:
    print("Error! n can't be negative.")
elif n == 0:
    print(0)
else:
    list = [0, 1]
    while True:
        n1 = list[len(list)-1]
        n2 = list[len(list)-2]
        if (n1+n2) > n:
            break
        else:
            list.append(n1+n2)
    print(list)