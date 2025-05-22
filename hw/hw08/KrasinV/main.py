from utils import * 
from models import *
print(list(filter (lambda str: not ("_" in str), dir())))

# def no_underscore(name):
#     return "_" not in name

# print(list(filter(no_underscore, dir())))
# print(dir())