def day_of_week(num):
    
    num = num % 7
    if num == 1:
        print("Monday")
    if num == 2:
        print("Tuesday")
    if num == 3:
        print("Wednesday")
    if num == 4:
        print("Thursday")
    if num == 5:
        print("Friday")
    if num == 6:
        print("Saturday")
    else:
        print("Sunday")

def main():
    try:
        num = int (input("Enter a number: "))
        result = day_of_week(num)
        print(f"day_of_week {result}")
    except Exception as e:
        print(f"Please enter a number{e}")  
        
        
        
