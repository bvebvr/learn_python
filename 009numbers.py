'''
Python numbers
int
float
complex
'''


a= 9
b= 8.7
c= 6j

print(type(a))
print(type(b))
print(type(c))

x=1
y=-1
z=1010101010

print(type(x))
print(type(y))
print(type(z))

x=2.50
y=2.5
z=-7.65

print(type(x))
print(type(y))
print(type(z))

x=2e4
y=98e5
z=9.66e99

print(type(x))
print(type(y))
print(type(z))

x=2+8j
print(x)
y=3j
z=-7j

print(type(x))
print(type(y))
print(type(z))

a= 9
b= 8.7
c= 6j

x=float(a) #convert fron int to float
y=int(b) #convert from float to int
z=complex(a) #convert from int to complex

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

import random #import the random module
print(random.randrange(101)) #display a random number from 0-100

def func():
    import random
    a=(50)
    while a in range (1,101):
        if a == 99:
            break
        else:
            a=random.randrange(1,101)
        print(a)

func()