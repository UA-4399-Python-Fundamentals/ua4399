import area


def main():

    print(
        "Which area you want to calculate?\n"
        "1. Triangle\n"
        "2. Rectangle\n"
        "3. Circle\n"
        "4. Exit\n"
    )
    while True:
        user_choice = input("Enter number 1-4: ")
        match user_choice:
            case "1":
                area.triangle_area()
            case "2":
                area.rectangle_area()
            case "3":
                area.circle_area()
            case "4":
                print("Bye")
                break
            case _:
                print("Wrong value")


main()
