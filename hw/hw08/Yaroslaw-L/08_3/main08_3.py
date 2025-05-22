from mod import area_r, area_t, area_c
def main():
    print("Choose the shape to calculate area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        l = input("Enter the length: ")
        h = input("Enter the height: ")
        result = area_r(l, h)
        print(f"Area of rectangle: {result}")
    elif choice == "2":
        b = input("Enter the base: ")
        h = input("Enter the height: ")
        result = area_t(b, h)
        print(f"Area of triangle: {result}")
    elif choice == "3":
        r = input("Enter the radius: ")
        result = area_c(r)
        print(f"Area of circle: {result}")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()