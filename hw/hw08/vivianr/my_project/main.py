import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from my_project.utils import *
from my_project.models import *

print(list(filter(lambda str: not ("__" in str), dir())))
