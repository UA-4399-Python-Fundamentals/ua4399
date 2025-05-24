# f =  open("../lesson13/data.txt", "r")
# f =  open("lessons/lesson14/data.txt", "r")
# print(f.read())

# try:
#     f = open("lessons/lesson14/data_2.txt", "w")
# finally:
# #     f.close()

# f =  open("lessons/lesson14/data.txt", "r")
# line = f.readline()
# print(line, f.tell())
# line = f.readline() # \n
# print(line, f.tell())
# print(f.readlines())
# f.seek(5)
# line = f.readline()
# print("temp:", line)

# # f.seek(0)


# f =  open("lessons/lesson14/data.txt", "r")
# for line in f:
#     print(line)
# f.close()

# with open("lessons/lesson14/data.txt", "r") as f:
#     for line in f:
#         print(line)


# with open("lessons/lesson14/out.txt", "a") as file:
#     import time
#     current_time = time.time()
#     file.write(str(current_time)+"\n")

#     time.sleep(3)
#     file.writelines(["test1\n", "TEST2", "te\nst3"])


import os
from dotenv import load_dotenv
from settings import name, key
load_dotenv()
print( os.getenv('key'))
print(name, key)



path = os.environ["PATH"]
print(path)
database_url = os.environ.get("DATABASE_URL", "localhost:5432")
print(database_url)


