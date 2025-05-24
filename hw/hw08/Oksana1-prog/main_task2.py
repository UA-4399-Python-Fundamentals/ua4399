import figures_task2
def get_numbers(prompt, count):
    while True:
        try:
            nums = list(map(float, input(prompt).split()))
            if len(nums) != count:
                print(f"Please enter exactly {count} numbers.")
            else:
                return nums
        except ValueError:
            print("Invalid input. Please enter numbers only.")
print("Choose a shape to calculate area:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")
choice = input("Enter 1, 2, or 3: ").strip()
if choice == '1':
    a, b = get_numbers("Enter sides a and b: ", 2)
    print("Area of rectangle:", figures_task2.rectangle_area(a, b))
elif choice == '2':
    a, h = get_numbers("Enter base and height: ", 2)
    print("Area of triangle:", figures_task2.triangle_area(a, h))
elif choice == '3':
    r, = get_numbers("Enter radius: ", 1)
    print("Area of circle:", figures_task2.circle_area(r))
else:
    print("Invalid choice.")