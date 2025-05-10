string = input("Input your string: ")

def calculate_characters(x):
    dictionary = {}
    
    for letter in x.lower():
        dictionary[letter] = x.count(letter)
    print(dictionary)

calculate_characters(string)