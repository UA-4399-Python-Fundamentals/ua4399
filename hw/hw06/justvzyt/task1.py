list1 = []
list2 = []
list3 = []
lists = [list1, list2, list3]

for i in range(1, 11):
    if i % 2 == 0:
        list1.append(i)
    if i % 2 != 0 and i % 3 == 0:
        list2.append(i)
    if i % 2 != 0 and i % 3 != 0:
        list3.append(i)

for i in lists:
    print(*i)