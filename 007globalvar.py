#Create variables inside and outside function.

#Create a global variable same variable name as inside function.
y = 'man'
def homo():
    y='woman' #variable inside a function
    print('A '+y)

homo()
print('A '+y) #variable outside a function (global variable)

#Create a global variable inside a function, use the "global" keyword.
z = 'human'
def glo():
    global z #"global" keyword inside a function can change the value of a global varible.
    z = 'animal'
glo()
print('Human is '+z)

#multiple variables and values on one line.
x,y,z = ('cat','dog','bird') 
print(x)
print(y)
print(z)

#multiple value, one variable
x=y=z='fish'
print(x)
print(y)
print(z)

'''
**list
**tuple
'''
#unpack a collection of values
animals=['cat','dog','bird','fish','snake','tiger','lion']
a,b,c,d,e,f,g=animals
print(animals)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
