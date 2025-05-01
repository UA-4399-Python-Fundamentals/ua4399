# for variable in "text":
#     print(variable)

# t = "text"
# while len(t) >= 0:
#     print("a",t)
#     t = t[1:]
# print("end")

# while True:
#     # f()
#     print("a")
#     import time
#     time.sleep(2)


# is_running = True

# while is_running:
#     text = input("Enter text (or 'exit' to quit): ")
#     if text.lower() == "exit":
#         is_running = False
#     else:
#         print(f"You entered: {text}")

# else:
#     print("Loop ended.")

# print("This will not be printed because the loop was exited with 'exit'.")

    
# start = 0
# finish = 10
# while start < finish:
#     print(f"{start=} {finish=}")
#     start += 1

# text = "text"

# i = 0
# while i < len(text):
#     print(text[i])
#     i += 1


# i = 10
# for x in i:#TypeError: 'int' object is not iterable
    # print(x)
# l = [1, 2, 3, [4, 5, 6], 7, 8, 9]

# for element in l:
#     print(element)
# else:
#     print("else")
# print("end")

# s = "string"
# for element in s:
#     print(element, end=" ")
# else:
#     print()

# s = {"a", "b", "c"}
# for element in s:
#     # print(element)
#     # print(element, end="\n")
#     print(element, end=" ")


# l = [1, 2, 3, [4, 5, 6], 7, 8, 9]


# print(list(range(10)))
# print(list(range(-10)))
# print(list(range(-10, 10)))
# print(list(range(-10, 10, 2)))
# # print(list(range(-10, 10, 2.5)))#TypeError: 'float' object cannot be interpreted as an integer
# print(list(range(1)))
# print(list(range(10, -50, -7)))
# print(list(range(-20, -50)))
# print(list(range(-50, -20)))


# print(1,2,3,4,5)
# print(1,2,3,4,5, sep=" ", end="\n")
# print(1,2,3,4,5, sep="->", end="\n")
# print(1,2,3,4,5, sep="->", end=" => ")
# print("text", end=" ==> ")
# print("text2")
# print("text3")
# print("text4")


list1 = [1, 2, 3, [4, 5], 6]

# for i in list1:
#     if isinstance(i, list):
#         i.append(7)
#     else:
#         i += 1

# print(list1)

# for i in range(len(list1)):
#     if isinstance(list1[i], list):
#         list1[i].append(77)
#     else:
#         list1[i] += 1
# print(list1)
# for i in list1:
#     print(list1)
#     # list1.append(len(list1))
#     list1.insert(0, len(list1))


# list2 =[
#     "text",
#     [1,2,3,4,5],
#     {1,2,3,4,5},
#     {"a": 1, "b": 2},
#     (1,2,3,4,5),
# ]

# for row in list2:
#     row_enumerate = list(enumerate(row))
#     print(row, row_enumerate, sep=" => ")
#     for element in row_enumerate:
#         print(element)

#     a, b = row_enumerate[0]
#     print(f"{a=} {b=} {row_enumerate[0]=}")
#     for index, element in row_enumerate:
#         print(index, element)

# d = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# for key in d:
#     print(key, d[key])
# print(f"{d.items()=}")
# for key, value in d.items():
#     print(key, value)

# d = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }

# for key, value in d.items():
#     print("start iterate")
#     print(key, value)
#     print("end iterate")
# else:
#     print("else")


# print("end")

# input_text = input("Enter text: ").split()
# print(f"{input_text=}")
# summa = 0
# text = ""

# for word in input_text:
#     if word.isdigit():
#         summa += int(word)
#     else:
#         text += word + " "

#     print(f"{word=}")
#     print(f"\t{summa=}")
#     print(f"\t{text=}")
#     if summa > 10:
#         print("Summa > 10")
#         break
# else:
#     print("end of loop")
#     print(f"{text=} {summa=}")

# print("======== end")


# input_text = input("Enter text: ").split()
# print(f"{input_text=}")
# summa = 0
# text = ""

# for word in input_text:
#     if word.isdigit():
#         summa += int(word)
#     else:
#         text += word + " "

#     print(f"{word=}")
#     if len(word) < 3:
#         print("Word length < 3")
#         continue
#     print(f"\t{summa=}")
#     print(f"\t{text=}")
    
# else:
#     print("end of loop")
#     print(f"{text=} {summa=}")

# print("======== end")


# for i in range(101):
#     if i % 2 == 0:
#         print(i)

# print(list(range(0, 101, 2)))


# number = 0
# while number < 100:
#     number += 2
#     print(number)

for i in range(101):
    if i % 2 != 0:
        continue
    print(i, end=" ")
print() 

for elem in range (101):
    if elem % 2 == 0:
        continue
    print(elem, end=" ")
print() 

print(tuple(range(101)))