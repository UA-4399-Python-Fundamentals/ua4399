# my_list = [1, 2, 3, 4, 5, 5, 5]
# print(my_list.pop())
# # my_list[5] = 4
# print(my_list[5])
# print(1 not in my_list)
# n_list = ["Happy", [1, 2, 3, 4, 5]]
# # print(n_list[0][1])
#
# print(my_list != n_list)
# #print(my_list[::-1])

# my_tuple = (1, 2, 3, 1,[1, 2, 3, 4, 5, 5, 5])
# print( my_tuple.count(1))
# print( my_tuple.index(2))

# my_set = {1,2,3,3,3,3}
# print(my_set)
#
# my_set = {1,2}
# print(my_set)
# my_set.add(3)
# print(my_set)
# my_set.update([2,3,4])
# print(my_set)

my_dict = {'name': 'Jack', 'Age': 26}
print(my_dict.get('name'))

squares = {x: x * x for x in range(6)}
print(squares)

d = {'name': 'Vasyl',
     'surname': 'Bilan',
     'id': '1',
     'task': 'run application'}
print(d)
for key in d:
    print(f"student {key} = {d[key]}")
for key, val in d.items():
    print(f"{key} = {val} .")
for key in d.keys():
    print(f"student {key} = {d[key]}")
