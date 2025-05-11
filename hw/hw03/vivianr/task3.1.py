import this
import codecs
zen = codecs.decode(this.s, 'rot_13')
count_better = zen.count("better")
count_never = zen.count("never")
count_is = zen.count("is")
zen_upper = zen.upper().replace("I", "&")
print("Count of 'better':", count_better)
print("Count of 'never':", count_never)
print("Count of 'is':", count_is)
print("\nModified text:\n", zen_upper)