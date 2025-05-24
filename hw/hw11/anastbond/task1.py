def process_age(age):

  if age < 0:
    raise ValueError('Enter a positive number')
  if age%2==0:
    return 'Age is even'
  elif age%2!=0:
    return'Age is odd'

def main():
    try:
      age = int(input('Enter your age'))
      result = process_age(age)
      print(result)
    except ValueError as e:
      print(e)

