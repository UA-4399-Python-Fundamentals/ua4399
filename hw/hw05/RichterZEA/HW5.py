# num = [1, 2, 3, 4, 5]
# for i in range (len(num)):
#     num[i] = float(num[i])
# print(num)

# x = int(input("Введіть число: "))
# a = 0
# b = 1
# while a <= n:
#     print(a)
#     a, b = b, a + b

n = int(input("Введіть число: "))
f = 1
for i in range(1, n + 1):
    f *= i
print(f)