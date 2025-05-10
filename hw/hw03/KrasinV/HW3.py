#HW3-1: Python Phylosofi in string format
print("\n")
print("Python Phylosophy :")
pp = """
1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex.
4.Complex is better than complicated.
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.
18.If the implementation is easy to explain, it may be a good idea.
19.Namespaces are one honking great idea -- let's do more of those!
20.Beautiful is better than ugly.
21.Explicit is better than implicit.
22.Simple is better than complex.
23.Complex is better than complicated.
24.Flat is better than nested.
25.Sparse is better than dense.
26.Readability counts.
27.Special cases aren't special enough to break the rules.
28.Although practicality beats purity.
29.Errors should never pass silently.
30.Unless explicitly silenced.
31.In the face of ambiguity, refuse the temptation to guess.
32.There should be one-- and preferably only one --obvious way to do it.
33.Although that way may not be obvious at first unless you're Dutch.
34.Now is better than never.
35.Although never is often better than *right* now.
36.If the implementation is hard to explain, it's a bad idea.
37.If the implementation is easy to explain, it may be a good idea.
38.Namespaces are one honking great idea -- let's do more of those!Beautiful is better than ugly.
39.Explicit is better than implicit.
40.Simple is better than complex.
41.Complex is better than complicated.
42.Flat is better than nested.
43.Sparse is better than dense.
44.Readability counts.
45.Special cases aren't special enough to break the rules.
46.Although practicality beats purity.
47.Errors should never pass silently.
48.Unless explicitly silenced.
49.In the face of ambiguity, refuse the temptation to guess.
50.There should be one-- and preferably only one --obvious way to do it.
51.Although that way may not be obvious at first unless you're Dutch.
52.Now is better than never.
53.Although never is often better than *right* now.
54.If the implementation is hard to explain, it's a bad idea.
55.If the implementation is easy to explain, it may be a good idea.
56.Namespaces are one honking great idea -- let's do more of those!"""
# Question to Lubhomye - What I cannot end condition and start from the new line ?
print(pp)
print("\n")

#HW3 Count number of words
find_never = print ("The Number of occurances 'never' =".upper(), pp.count('never'), end='\n')
find_better = print ("The Number of occurances 'better' =".upper(), pp.count('better'), end='\n')
find_is = print ("The Number of occurances 'is' =".upper(), pp.count('is'), end='\n')
print("\n")

#HW3 Replace i with &
message = "Replace 'i' with '&' below:"
print(message)
text_replace = pp.replace('i','&')
print(text_replace, end='\n\n')

#HW3-2: 4-digit operation
#A four-digit natural number is specified:
enter_number = input("Enter 4-digit whole number: ")
# Question to Lubhomyr - Why below not letting me show with separator on each individual like
# print("Digit1- ", enter_number[0], "Digit2- ", enter_number[1], "Digit3- ", enter_number[2], "Digit4- ", enter_number[3], sep='\r')
print("Digit1:", enter_number[0])
print("Digit2:", enter_number[1])
print("Digit3:", enter_number[2])
print("Digit4:", enter_number[3], end='\n')

# - find the product of the digits of this number
product = int(enter_number[0])*int(enter_number[1])*int(enter_number[2])*int(enter_number[3])
print("Product of 4-digits: ",product, end='\n')

# - write the number in reverse order
print("Reverse order of 4-digit number: ",str(product)[::-1])

#- in ascending order, you need to sort the numbers included in the given number

number_for_order = [enter_number[0], enter_number[1], enter_number[2], enter_number[3]]
number_ordered = sorted (number_for_order)
print ("Ascend order of numbers in the given number: ", number_ordered, end='\n')
print("\n")

#HW3-3: Interchange the values of two variables without using the third variable.
print("Interchange the values of two variables without using the third variable:", end='\n')
val1 = 4
val2 = 3
val1,val2 = val2,val1
print(val1,val2)