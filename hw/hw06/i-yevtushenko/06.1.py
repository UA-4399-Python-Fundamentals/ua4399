rez1 = []
for i in range (1,10):
    if i % 2 == 0:
        rez1.append(i)
print(rez1)

rez2 = []
for i in range (1,10):
    if i % 2 != 0 and i % 3 == 0:
        rez2.append(i)
print(rez2)

rez3 = []
for i in range (1,10):
    if i % 2 != 0 and i % 3 != 0:
        rez3.append(i)
print(rez3)