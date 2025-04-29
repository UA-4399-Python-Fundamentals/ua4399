number = int(input("Enter number: "))

f = 1
mylist = []
for i in range(1, number+1):
    mylist.append(i)
    f *= i

print(*mylist, sep="*", end=f"={f}")