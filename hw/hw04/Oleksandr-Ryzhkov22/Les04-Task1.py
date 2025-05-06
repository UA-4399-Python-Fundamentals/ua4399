Ca = input ('What is the temperature in C*?')
C = float (Ca)
Fa = C * 9/5 + 32
F = float (Fa)
if C<-275:
    print ("Error: Temperature below absolute zero (-273.15°C)")
else:
    print (F)