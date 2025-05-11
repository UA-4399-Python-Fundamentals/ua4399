#Create a list that contains elements of integer type, change the type of these elements to floating type using the loop and print the list.
int = [1, 2, 3, 4, 5]
for x in range(len(int)):
    int[x] = float(int[x])
print(int)