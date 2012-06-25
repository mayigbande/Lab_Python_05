print "problem 1"
input=int(raw_input("enter a number: "))
def factorial(n):
    f=1
    while n>0:
        f=f*n
        n=n-1
    return f
factorial(input)
print factorial(input)
print 'problem 2'
number=int(raw_input('enter a number'))
#new_number=number-2
b=[1,1]
def fibonacci(number):
    for i in range(2,number):
       a=b[i-1]+b[i-2]
       b.append(a)
    return b
fibonacci(number)
print b,
         
print "problem 3"

def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print "its prime"
        return True
    else:
        print 'nt prime'
        return False
prime(3)

