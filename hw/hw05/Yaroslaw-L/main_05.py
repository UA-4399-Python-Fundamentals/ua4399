# 05.1 int to float
our_list = []
for i in range(0, 60):
    i +=1
    our_list.append(i)
for x in range(len(our_list)):
    our_list[x] = float(our_list[x])
print(our_list)

# 05.2 Fibonacci
n = int(input("Type the last number for Fibonacci sequence: "))
a, b = 0, 1
while a <= n:
    print(a)
    a, b = b, b+a

# 05.3 factorial
m = int(input("Type number to calculate factorial for it: "))
result = 1
for i in range (2, m+1):
    result *= i
print(f"{m}! equal: \n{result}")



