from math import pow, pi
import area

def main():
  try:
    user_choice = input(' Which area you want to calc?\n Rectangle, triangle, or circle?').lower()
    if user_choice == 'rectangle':
      a = float(input(" Enter side A lenghth"))
      b = float(input(" Enter side B lenghth"))
      result = area.rectangle_area (a, b)
      print(result)
    elif user_choice == 'triangle':
      a = float(input(" Enter side A lenghth"))
      b = float(input(" Enter side B lenghth"))
      result = area.triangle_area (a, b)
      print(result)
    elif user_choice == 'circle':
      r = float(input(" Enter R length"))
      result = area.circle_area (r)
      print(result)
    else:
      print("Invalid choice.")
  except ValueError:
    print("Error: Please enter valid numbers.")

if __name__ == "__main__":
  main()
