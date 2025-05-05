import re

def password_val(password):
  has_lowercase = bool(re.search(r'[a-z]', password))
  has_uppercase = bool(re.search(r'[A-Z]', password))
  has_digit = bool(re.search(r'[0-9]', password))
  has_special = bool(re.search(r'[$#@]', password))
  if len(password) < 6 or len(password) > 16:
    return False, "Unappropraite length."

  if has_lowercase == False :
    return False, "Password doesn't have lowercase."
  elif has_uppercase == False:
    return False, "Password doesn't have uppercase."
  elif has_digit == False:
    return False, "Password doesn't have a digit."
  elif has_special == False:
    return False, "Password doesn't have a special digit."
  
  else:
    return True, "Password validation successful."

password = input("Enter your passord.\n")

is_valid, message = password_val(password)
print(message)
