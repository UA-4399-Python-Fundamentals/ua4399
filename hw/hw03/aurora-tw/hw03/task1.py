#Task 1
PY_PHYL = "Beautiful is better than ugly. \n\
Explicit is better than implicit. \n\
Simple is better than complex.\n\
Complex is better than complicated.\n\
Flat is better than nested.\n\
Sparse is better than dense.\n\
Readability counts.\n\
Special cases aren't special enough to break the rules.\n\
Although practicality beats purity.\n\
Errors should never pass silently.\n\
Unless explicitly silenced.\n\
In the face of ambiguity, refuse the temptation to guess.\n\
There should be one-- and preferably only one --obvious way to do it.\n\
Although that way may not be obvious at first unless you're Dutch.\n\
Now is better than never.\n\
Although never is often better than *right* now.\n\
If the implementation is hard to explain, it's a bad idea.\n\
If the implementation is easy to explain, it may be a good idea.\n\
Namespaces are one honking great idea -- let's do more of those!"

#Task 1 Part 1
num_of_better = PY_PHYL.count("better")
num_of_never = PY_PHYL.count("never")
num_of_is = PY_PHYL.count("is")

print(f"The word \"better\" is found {num_of_better} times.\n" 
      f"The word \"never\" is found {num_of_never} times.\n"
      f"The word \"is\" is found {num_of_is} times.\n"
      )

#Task 1 Part 2
print(f"All text in uppercase:\n{PY_PHYL.upper()}\n")

#Task 1 Part 3
py_phyl_rep = PY_PHYL.replace("i","&")
print(f"Symbol \"i\" is replaced by \"&\":\n{py_phyl_rep}")






#upper()
