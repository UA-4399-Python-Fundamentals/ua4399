#args and kwargs
#def my_funk(a,b,*args,e=10,f=20, **kwargs):
    #print(f"{a= } {b= } {args= } {e= } {f= } {kwargs= }")

#g="global"
#def outer():
    #l="local"
    #def inner():
        #l="local_inner"
        #print(l,g)
    #inner()
    #print(l,g)
#print (outer ())
#def print_i (start):
    #print(start)
    #print_i(start+1)
#print_i(-99)

#def temp_recursion(max_recursion):
    #import sys
    #current=sys.getrecursionlimit()
    #sys.setrecursionlimit(max_recursion)
    #def dec(funk):
        #def inner(*a,**k):
            #r=funk(*a,**k)
            #return r
        #return inner
    #sys.setrecursionlimit(current)
    #return(dec)
    #def fibo(n):
        #if n < 2:
            #return 1
        #else:
            #return fibo(n-1)+fibo(n-2)
    #print(fibo(1))
    #print(fibo(2))
    #print(fibo(3))
    #print(fibo(4))
    #print(fibo(5))
    #def sum(a,b):
        #return a+b

    #print(sum(10,20))
#sum=lambda a,b: a**2+b**2
#print (sum(10,20))
#my_func=lambda x: x if x>5 else x**2*my_func(10)
#print(my_func(2))
#def my_func(input_message,numb=1):
    #print(input_message*numb)
#my_func('Hello')
#my_func('Hi', 5)
#def my_func(first_param=3,second_param=1):
    #first_param =first_param+second_param
    #second_param+=1
    #print(first_param, second_param)
#my_func(second_param=1,first_param=3)
#my_list=[lambda x: x**2,
         #lambda x: x**3,
         #lambda  x: x**4]
#for item in my_list:
    #print(item(5))
#def output_param(x,y,z):
    #print(x,y,z)
#my_tuple=(1,2,3,)
#output_param(*my_tuple)
#counter=5
#def my_func():
    #counter=8
    #print(counter)
#my_func()
#print(counter)











