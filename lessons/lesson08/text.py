import re
text = """Okay, here's a longer and more readable text in English that includes numbers and special characters:

"Hello there! Today is May 1st, 2025, and the weather in Lviv is fantastic! I'm really looking forward to our meeting later at 7:30 PM near 'Chocolate Dream' cafe. Don't forget! We have a lot to discuss regarding Project Alpha (version 2.5). Please bring the latest report (dated 04/28/2025) and your notes. It's crucial that we finalize the budget ($15,000 estimated) and the timeline. Any questions before then? Feel free to email me at user.example@email.com or call me at +380 123 456 7890. See you soon! #Lviv #spring #projectmanagement"""


template = r"[abc]"
print(re.findall(template, text))

template = r"[a-zA-Z]"
print(re.findall(template, text))

template = r"\d"
print(re.findall(template, text))

template = r"\d.\d"
print(re.findall(template, text))
template = r"\d:\d"
print(re.findall(template, text))
template = r"t$"
print(re.findall(template, text))
template = r"[a-z]{4}"
print(re.findall(template, text))
template = r"[a-z]{4,7}"
print(re.findall(template, text))