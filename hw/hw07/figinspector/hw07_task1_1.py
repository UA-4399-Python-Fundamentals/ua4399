def largest_num(x, y):
    """
    This function returns largest number
    """
    return x if x > y else y

print(largest_num(45, 7))
print(largest_num(-5, 0))
print(largest_num(1.222, 1.235))

# 
# як практика, пишу такий варіант, щоб краще розібратися з лямбдою
# це по факту, функціональний виріз js
# 
# largest_num = lambda x, y: x if x > y else y
# print(largest_num(65, 7657))
# print(largest_num(25529, 24126))