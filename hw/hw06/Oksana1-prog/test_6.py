#l=[1,2,3,4,5,[1,2,3,4],list("hello"),list((1,2,3)),[1,2,3], list]
#print(type(l),l)
#ll=l[3:-2]
#print(ll)
#ll=l[1:-2]
#print(ll)
#ll=l[1:-3]
#print(ll)
#ll=l[1:-1]
#print(ll)
#a=[1,2,3]
#b=[1,2,3]
#l=[a,b,7,8,9]
#print(l)
#ll=l+l
#print(ll)
#ll[0]=100
#print(ll)
#ll[1].append(1000)
#print(ll)
#l=[1,2,3,4,5]*3 #матриця
#print(l)
#l=[[]*3]*3
#print(l)
#l[0].append(100)
#print(l)
#l=[]
#for i in range(3):
   #l.append([])
#rint(l)
#[0].append(100)
#rint(l# )
#l=[1,2,3]
#print(l)
#l.append(l)
#print(l)
#print(l[3])
#l[3][3][3][3][3][3][3][3][3][3][3][1]=100
#print(l)
#l=[1,2,3, [4,5,6],"7,8,9,"]
#print(1 in l)
#print(1 not in l)
#print([method for method in dir(list) if not method.startswith("_")])
#l=[]
#print(l)
#l.append(1)
#print(l)
#l.extend([5,6,7])
#print(l)
#l.append([5,6,7])
#print(l)
#l.insert(0,100)
#print(l)
#print(l.count(1))
#print(l.count(100))
#print(l.count(1000))
#print(len(l))
#e=l.pop()
#print(l,e)
#e=l.pop(2)
#print(l,e)
#l.append(100)
#l.remove(100)
#l.insert(3,100)
#l.insert(3,100)
#print(l.index(100))
#print(l.index(100,3))
#l=[1,2,3,4,5]
#print(l)
#l.clear()
#print(l)
#a=[1,2,3,4,5]
#l=[1,2,3,4,5,a]
#b=l.copy()
#print(id(l),l)
#print(id(b),b)
#print(l is b)
#print(l==b)
#a[0]=100
#print(id(l),l)
#print(id(b),b)
#from copy import deepcopy
#d=deepcopy(l)
#print(id(l),l)
#print(id(b),b)
#print(id(d),d)
#print("=="*20)
#a[2]=200
#print(id(l),l)
#print(id(b),b)
#print(id(d),d)
#l.reverse()
#print(id(l),l)
#l.sort()
#print(id(l),l)
#l=[3,34,56,56,8]
#l.sort()
#print(id(l),l)
#l=(1,2,35)
#print(any(l))
#from random import randint
#n=10
#l=[randint(1,100) for i in range(n)]
#t=tuple(l)
#print(f"list:{l} size:{len(l) sizeof{l._sizeof_()}")

#s=set()
#print(type(s),s)
#s=set("hello")
#print(type(s),s)
#s={1,2,3,4,5}
#print(type(s),s)
#s.add(100)
#print(s)
#print(s.pop())
#print(s)
#text="hello world"
#s=set(text)
#d={}
#while s:
    #c=s.pop()
    #d[c]=text.count(c)
#print(d)
#s.update((4,5,6,7))
#print(s)
#d=dict()
#print(type(d),d)
#d=dict([(1,1), ("a",2), (True,4)])
#print(type(d),d)
#d={
    #1:1,
    #"a":2,
    #False:4,
    #(1,2):5,
#}
#print(type(d),d)

#list1 = ['xyz', 'zara', 'PYnative']
#print (max(list1))
#sum = 0
#counter = 0
#numbers = [22, 55, 111, 555]
#while numbers[counter] < 100:
  #sum = sum + numbers[counter]
  #counter = counter + 1
#print(sum)
#my_list = ["Hello", "Python"]
#print("-".join(my_list))

#aList = ["PYnative", [4, 8, 12, 16]]
#print(aList[0][1])
#print(aList[1][3])