#Task 1

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(l)):
    l[i] = float(l[i])

print(l)

#Task 2

fibo_num = int(input("Enter a number: "))

f1, f2 = 1, 1
print(f"{f1}\n{f2}")
while fibo_num > f2:
    f1, f2 = f2, f1 + f2
    print(f2)

#Task 3

fact_num = int(input("Enter a number: "))
res = 1
for i in range(1, fact_num+1):
    res *= i

print(res)