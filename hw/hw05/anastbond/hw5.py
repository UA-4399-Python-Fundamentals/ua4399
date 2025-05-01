# TASK1

# my_list = [1,2,3,4,5]
# i = 0
# while (my_list[i] < len(my_list)):
#   my_list[i] = float(my_list[i])
#   print(my_list[i])
#   i+=1

# TASK2

# n = 6
# thislist = [0, 1]
# for i in range(2, n):
#   number = thislist[i-1] + thislist[i-2]
#   thislist.append(number)
# for n in thislist:
#   print(n)

#TASK3

num = 2
flist = []
for i in range(1, num):
  flist.append(i)
i = 0
result = 1
for i in range (1, num+1):
  result *= i

print(result)
