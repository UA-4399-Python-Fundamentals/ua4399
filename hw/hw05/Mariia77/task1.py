a = [1, 2, 3, 4, 5]
# for by value
for i in a:
    b = float(i)
    print(b)
# for by index
for i in range(len(a)):
    b = float(a[i])
    print(b)
# for with save list
b = [float(i) for i in a]
print(b)
