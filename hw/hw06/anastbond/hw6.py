#TASK1
nlist = list(range(1, 11))
print (nlist)
even = [num for num in nlist if num%2 == 0]
three = [num for num in nlist if num%3 == 0]
two_three = [num for num in nlist if num % 2 != 0 and num % 3 != 0]

message = f" even = {even}\n divided by 3 = {three}\n not divided by 2&3 = {two_three}"
print(message)

#TASK2
while 1:
  login = input('Enter your login\n')
  if login.lower() == 'first':
    print('Hello, user')
    break
  else:
    print('Error')
