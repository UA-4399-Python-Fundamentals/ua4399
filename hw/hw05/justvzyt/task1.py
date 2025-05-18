list = input("Input some integers: ").split()

for i in range(len(list)):
    list[i] = float(list[i])
    
print(f"New list: ", list)