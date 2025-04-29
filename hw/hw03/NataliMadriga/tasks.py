#TASK 1
text = "Simple is better than complex"
print(text.upper())
print(text.replace("i", "&"))
text = "Simple is better than complex"
print(f"The 'better' word count is {text.count('better')}\n"
      f"The 'never' word count is {text.count('never')}\n"
      f"The 'is' word count is {text.count('is')}")

#TASK 2
number = 57681;
s = str(number)
#product
print(int(s[0]) * int(s[1]) * int(s[2]) * int(s[3]) * int(s[4]))
#revers
print(int(s[::-1]))
#sort
print(''.join(sorted(str(number))))

#TASK 3
a = 5
b = 10
a, b = b, a
print(a)
print(b) 
