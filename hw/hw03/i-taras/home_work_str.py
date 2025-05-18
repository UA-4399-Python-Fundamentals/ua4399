
# # ___________________________________________1__________________________________________________________


# philosophy_py = """Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.[c]
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than right now.[d]
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea – let's do more of those!"""

# # ___________________________________________1.1__________________________________________________________

# count_dict = {}

# key_better = 'better'
# key_never = 'never'
# key_is = 'is'

# value_better = philosophy_py.count(key_better)
# value_never = philosophy_py.count(key_never)
# value_is = philosophy_py.count(key_is)

# count_dict[key_better] = value_better
# count_dict[key_never] = value_never
# count_dict[key_is] = value_is

# for key, value in count_dict.items():
#     print(f"{key} =  {value}")


# # ___________________________________________1.2__________________________________________________________

# upper_philosophy = philosophy_py.upper()

# print(upper_philosophy)


# # ___________________________________________1.3__________________________________________________________

# replace_philosophy = philosophy_py.replace('I', '&').replace('i', '&')

# print(replace_philosophy)




# # ___________________________________________2__________________________________________________________

# number = input("Enter a four-digit number: ")


# # ___________________________________________2.1__________________________________________________________

# result = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])

# print(result)


# # ___________________________________________2.2__________________________________________________________

# print(number[::-1])


# # ___________________________________________2.3__________________________________________________________

# nuber_sort = sorted(number)
# print(nuber_sort)



# ___________________________________________3__________________________________________________________

# a = 5
# b = 10

# a, b = b, a

# print("a =", a)
# print("b =", b)

first_name = "television"
hobby = "homer"
tmp = first_name
first_name = hobby
hobby = tmp
print(f"T{first_name[1:3]} likes to watch {hobby[4:]}")