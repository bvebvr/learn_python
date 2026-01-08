#Many statements.
print("Learning Python.")
print('Happy new year.') #Single quote are also used for comments.
print('Have a good year.')

#I have 3 statements use semi-colon in one line to separate them.
print("Learning Python."); print('Happy new year.'); print('Have a good year.')

#Use end= parameter for print multiple words on the same line.
print('first', end=' ')#Use space in quotes for better readablity.
print('last')

#Print numbers, also do math. (not in quotes)
print(7)
print(7+3)
print(5*5)
print(2**3)
print(100/10)

#To combine text and numbers in one output by separate them with comma [,].
print('4x2=', 4*2)

#Variables has been set data type.
x = (77) #type int
y = 'Years old' #type str
print (x, y)

# Specify data type of variables with Casting.
a = str(78) #'78'
b = int(79) #79
c = float(80) #80.0
print(a, b, c)

#To get data type of variables.]
print (type(x))
print (type(y))
print (type(a))
print (type(b))
print (type(c))

#Variables name are Case-sensitive.
X = 81
Y = 82
print(x, y, X, Y) #X and Y will not overwrite x and y.

#I can declare string variables with single quotes or double quotes.
z = ("babe")
print (z)
z = 'babe'
print (z)
# '' and "" are the same.
