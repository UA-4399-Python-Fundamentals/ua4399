''' Home work 03 task1.1'''

"Task"

# You need to write Python's philosophy in the string format:
# - find separately the number of occurrences of the words
# - "better", "never" and "is" in the given line
# - you need to display all text in uppercase (all letters in uppercase)
# - replace all occurrences of the symbol “i” with “&”

"Declared variables"
philosohty_str = (
    "The Zen of Python, by Tim Peters\n"
    "1.Beautiful is better than ugly.\n"
    "2.Explicit is better than implicit.\n"
    "3.Simple is better than complex.\n"
    "4.Complex is better than complicated.\n"
    "5.Flat is better than nested.\n"
    "6.Sparse is better than dense.\n"
    "7.Readability counts.\n"
    "8.Special cases aren't special enough to break the rules.\n"
    "9.Although practicality beats purity.\n"
    "10.Errors should never pass silently.\n"
    "11.Unless explicitly silenced.\n"
    "12.In the face of ambiguity, refuse the temptation to guess.\n"
    "13.There should be one-- and preferably only one --obvious way to do it.\n"
    "14.Although that way may not be obvious at first unless you're Dutch.\n"
    "15.Now is better than never.\n"
    "16.Although never is often better than *right* now.\n"
    "17.If the implementation is hard to explain, it's a bad idea.\n"
    "18.If the implementation is easy to explain, it may be a good idea.\n"
    "19.Namespaces are one honking great idea -- let's do more of those!\n"
    "20.Beautiful is better than ugly.\n"
    "21.Explicit is better than implicit.\n"
    "22.Simple is better than complex.\n"
    "23.Complex is better than complicated.\n"
    "24.Flat is better than nested.\n"
    "25.Sparse is better than dense.\n"
    "26.Readability counts.\n"
    "27.Special cases aren't special enough to break the rules.\n"
    "28.Although practicality beats purity.\n"
    "29.Errors should never pass silently.\n"
    "30.Unless explicitly silenced.\n"
    "31.In the face of ambiguity, refuse the temptation to guess.\n"
    "32.There should be one-- and preferably only one --obvious way to do it.\n"
    "33.Although that way may not be obvious at first unless you're Dutch.\n"
    "34.Now is better than never.\n"
    "35.Although never is often better than *right* now.\n"
    "36.If the implementation is hard to explain, it's a bad idea.\n"
    "37.If the implementation is easy to explain, it may be a good idea.\n"
    "38.Namespaces are one honking great idea -- let's do more of those!\n"
    "39.Explicit is better than implicit.\n"
    "40.Simple is better than complex.\n"
    "41.Complex is better than complicated.\n"
    "42.Flat is better than nested.\n"
    "43.Sparse is better than dense.\n"
    "44.Readability counts.\n"
    "45.Special cases aren't special enough to break the rules.\n"
    "46.Although practicality beats purity.\n"
    "47.Errors should never pass silently.\n"
    "48.Unless explicitly silenced.\n"
    "49.In the face of ambiguity, refuse the temptation to guess.\n"
    "50.There should be one-- and preferably only one --obvious way to do it.\n"
    "51.Although that way may not be obvious at first unless you're Dutch.\n"
    "52.Now is better than never.\n"
    "53.Although never is often better than *right* now.\n"
    "54.If the implementation is hard to explain, it's a bad idea.\n"
    "55.If the implementation is easy to explain, it may be a good idea.\n"
    "56.Namespaces are one honking great idea -- let's do more of those!\n"
)

"Declared variables for 'better', 'never' and 'is' counter"
better_counter = philosohty_str.count("better")
never_counter = philosohty_str.count("never")
is_counter = philosohty_str.count("is")

"Output of the task result"
print(f"In the Zen of phyton text word 'better' appears {better_counter} times, " 
      f"word 'never' appears {never_counter} times, "
      f"word 'is' appears {is_counter} times")

"Output all text in uppercase"
print(philosohty_str.upper())

"replace all occurrences of the symbol “i” with “&”"
print(philosohty_str.replace("i","&"))
