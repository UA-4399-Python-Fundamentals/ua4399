def is_isogram(word):
    word = word.lower()
    return len(set(word)) == len(word)


def mean(number):
    digits = [int(d) for d in str(number)]
    return round(sum(digits) / len(digits))


def integer_boolean(binary_number):
    return [bool(int(i)) for i in str(binary_number)]


def count_vowels(word):
    vowels = 'aeiou'
    word = word.lower()
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count


var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)
