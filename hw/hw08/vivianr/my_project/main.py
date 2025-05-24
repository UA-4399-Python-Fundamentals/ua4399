from my_project.utils import *
from my_project.models import *

print(list(filter(lambda str: not ("__" in str), dir())))
