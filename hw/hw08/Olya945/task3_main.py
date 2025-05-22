import math
from task3_area_calculator import rectangle_area, triangle_area, circle_area

def main():
    print("=== ПРОГРАМА ЗАПУЩЕНА ===")
    print("Програма для обчислення площі фігур")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")

    choice = input("Оберіть фігуру для обчислення її площі (1, 2 або 3): ")

    if choice == "1":
        lenght = float(input("Введіть довжину прямокутника: "))
        width = float(input("Введіть ширину прямокутника: "))
        area = rectangle_area(lenght, width)
        print(f"Площа прямокутника: {area}")

    elif choice == "2":
        base = float(input("Введіть основу трикутника: "))
        height = float(input("Введіть висоту трикутника: "))
        area = triangle_area(base, height)
        print(f"Площа трикутника: {area}")
    
    elif choice == "3":
        radius = float(input("Введіть радіус кола: "))
        area = circle_area(radius)
        print(f"Площа кола: {area}")
    
    else:
        print("Невірний вибір.")

if __name__ == "__main__":
    main()    

print("=== ПРОГРАМА ЗАВЕРШЕНА ===")




   