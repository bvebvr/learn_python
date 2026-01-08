myvar='Cat'
my_var =  'Cat'
_my_var = 'Cat'
myVar = 'Cat'
MYVAR = 'Cat'
myvar2 = 'Cat'
my_Var = 'Cat'
print (myvar,my_var,_my_var,myVar,MYVAR,myvar2,my_Var)

"""
Rules for Python variables:
1. Start with a letter or underscore.
2. Cannot start with a number.
3. Only contain alpha-numeric characters and underscore. [ A-z, 0-9, _ ]
4. Case sensitive [DUCK, duck, Duck : are different variables]
5. Variables are cannot be any of Python Keywords.
"""

myVariableName = 'Cats' #Camel Case: Starts with a capital letter exceept the first.
MyVariableName = 'Cats' #Pascal Case: Starts with a capital letter.
my_variable_name = 'Cats' #Snake Case: separated by an underscore.

#output variables
print(myVariableName)
print(MyVariableName)
print(my_variable_name)

print(myVariableName, MyVariableName, my_variable_name)

_myVariableName = 'Dogs ' #Camel Case: Starts with a capital letter exceept the first.
_MyVariableName = 'Dogs ' #Pascal Case: Starts with a capital letter.
_my_variable_name = 'Dogs ' #Snake Case: separated by an underscore.

print(_myVariableName+_MyVariableName+_my_variable_name) #also can use the + operator to output multiple variables.

U = 8
u = 10
print(U*u)
print(u, _my_variable_name+'and',U, my_variable_name)
print('Cats and dogs are', U+u, 'in total.')
