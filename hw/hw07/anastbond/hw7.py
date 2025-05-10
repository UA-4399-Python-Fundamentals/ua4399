#TASK1

def return_largest (num1, num2):
  """This function return the largest number from two numbers"""
  if num1>num2:
    return num1
  elif num2>num1:
    return num2
  else:
    return 'Equal'

#TASK2

def rectangle_area (a, b):
  c = a*b
  return c

def triangle_area (a, b):
  c = (a*b)/2
  return c
  
def circle_area (r):
  c = 3.14*r**2
  return c

def area_program ():
  try:
    user_choice = input(' Which area you want to calc?\n Rectangle, triangle, or circle?').lower()
    if user_choice == 'rectangle':
      a = float(input(" Enter side A lenghth"))
      b = float(input(" Enter side B lenghth"))
      return rectangle_area (a, b)
    elif user_choice == 'triangle':
      a = float(input(" Enter side A lenghth"))
      b = float(input(" Enter side B lenghth"))
      return triangle_area (a, b)
    elif user_choice == 'circle':
      r = float(input(" Enter R length"))
      return circle_area (r)
  except ValueError:
    return -1
  
  #TASK3

def character_counter (inp_str):
  text = inp_str.lower()
  counter = {}
  for word in text:
      if word in counter:
          counter[word] += 1
      else:
          counter[word] = 1
  return counter


