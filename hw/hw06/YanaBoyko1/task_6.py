#task1
even_nums = [i for i in range(1, 11) if i%2==0]
print(even_nums)

odd_nums = [i for i in range(1, 11, 2) if i%3==0]
print(nums)

nums = [i for i in range(1, 11) if i%2 !=0 and i%3 != 0 ]
print(nums)

#task2
output_value = input("Enter: ")

while output_value != "First":
    print("Error")
    output_value = input("Enter: ")

print("Hello")
