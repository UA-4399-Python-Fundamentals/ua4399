# import this

ZEN_OF_PYTHON = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

count_better = ZEN_OF_PYTHON.lower().count('better')
print(f"Better occurs {count_better} in this text")

count_never = ZEN_OF_PYTHON.lower().count('never')
print(f"Never occurs {count_never} in this text")

count_is = ZEN_OF_PYTHON.lower().count('is')
print(f"Is occurs {count_is} in this text")

zen_to_uppercase = ZEN_OF_PYTHON.upper()
print(zen_to_uppercase)

replace_i = ZEN_OF_PYTHON.lower().replace('i', '&')
print(replace_i)
print(f"'&' has been replaced {replace_i.count('&')} times")