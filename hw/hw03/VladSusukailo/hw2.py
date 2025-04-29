num = 6768
s = str(num)
summ = 0
for i in s:
    summ += int(i)
res = int(str(summ)[::-1])
sort = sorted(s)


print(f"Задане число: {num}")
print(f"Добуток чисел: {summ}")
print(f"Зворотній порядок: {res}")
print(f"Сортовані числа: {sort}")
