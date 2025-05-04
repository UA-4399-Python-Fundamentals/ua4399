def count_characters(s):
    
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result

word = input("Напишіть слово:")
print(count_characters(word))  
