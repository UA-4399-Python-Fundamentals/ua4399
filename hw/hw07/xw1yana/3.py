def calcucale_characters(i):
    count = {}
    for char in i:
        count[char] = count.get(char,0) + 1
    return count
