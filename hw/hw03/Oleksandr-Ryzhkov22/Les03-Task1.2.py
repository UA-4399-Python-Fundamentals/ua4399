x = 3957
a=x%10
b=x//10
c=b%10
d=b//10
e=d%10
f=d//10
g=a*c*e*f
print (g)
sorted = sorted([a,c,e,f])
print (sorted)
n=g%10
m=g//10
l=m%10
o=m//10 
ansver=[n,l,o]
ansver.sort(reverse=True)
print (ansver)