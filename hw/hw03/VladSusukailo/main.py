from dataclasses import replace

text = "Beautiful is better than ugly.".upper()
word_of_text = []
word = ""
for i in text:
    if i == " ":
        word_of_text.append(word)
        word = ""
    word += i

print(word_of_text)
print(word_of_text.count(" BETTER"))
print(word_of_text.count(" IS"))
print(word_of_text.count(" NEVER"))
replace_text = text.replace("I", "&")
print(replace_text)
