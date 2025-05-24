import re
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$]).+$'

password = input('Enter your password to check: ')
if not re.match(pattern, password):
    print ('your password must containe [a-z],[A-Z],[!@#$] and number')
elif not 6 < len(password) < 16:
    print('password length must be 6-16 symbols')
else:
    print('you password is valid')