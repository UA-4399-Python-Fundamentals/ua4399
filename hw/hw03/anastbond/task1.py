# TASK1
string = "Beautiful is better than ugly."

def zen_count (string):
  better_c = never_c = is_c = 0
  clean_str = string.lower()
  words = clean_str.split()
  for i in words:
    clean_word = i.strip('.,!-')
    if (clean_word == 'better'):
      better_c += 1
    elif (clean_word == 'never'):
      never_c += 1
    elif (clean_word == 'is'):
      is_c +=1
  ready_string = string.replace('i', '&')
  answer = f"better = {better_c}\nnever = {never_c}\nis = {is_c}"
  print(answer)

  return ready_string.upper()


result = zen_count(string)
print(result)

# TASK2
numbers = [8, 4, 1, 9]
sorted_ascending = sorted(numbers)
sorted_descending = sorted(numbers, reverse=True)
print(sorted_ascending)
print(sorted_descending)

product = 1
for num in numbers:
    product *= num
print(product)

# TASK3
var1 = 8
var2 = 9
print(var1, var2)

var1, var2 = var2, var1
print(var1, var2)



