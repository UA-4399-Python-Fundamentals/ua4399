def count_characters(s):
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result
user_input = input("Enter a string: ")
print(count_characters(user_input))