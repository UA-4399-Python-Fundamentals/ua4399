#task1
list = [1,3,5,6,7]

for i in range(len(list)):
    list[i] = float(list[i])
print(list)

#task2
a, b = 0,1
n=int(input("Enter fibonacci number: "))

while a <= n:
    print(a)
    a, b = b, a + b

#task3
n=int(input("Enter factorial number: "))
res = 1

for i in range(1, n + 1):
    res = res * i
print(res)
