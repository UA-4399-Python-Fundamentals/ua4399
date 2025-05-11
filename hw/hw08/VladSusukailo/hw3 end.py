import hw3

def main():
    print("Оберіть фігуру для обчислення площі:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Круг")

    choice = input("Введіть номер (1-3): ")

    if choice == "1":
        a = float(input("Введіть довжину: "))
        b = float(input("Введіть ширину: "))
        print("Площа прямокутника:", hw3.rectangle_area(a, b))
    elif choice == "2":
        a = float(input("Введіть основу: "))
        b = float(input("Введіть висоту: "))
        print("Площа трикутника:", hw3.triangle_area(a, b))
    elif choice == "3":
        r = float(input("Введіть радіус: "))
        print("Площа круга:", hw3.circle_area(r))
    else:
        print("Невірний вибір.")

if __name__ == "__main__":
    main()