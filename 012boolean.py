#boolean values
print(6==9)
print(6>9)
print(6<9)
#Python returns the Boolean answer (True or False).

#run booleans in a condition in an if statement.
x = 100
y = 50
if x > y:
    print(x, "is greater than", y)
else:
    print(x, "is not greater than", y)

#bool() evaluate any value
print(bool("Smith")) #Evaluate str
print(bool(32)) #Evaluate number

x='Above'
y=2
print(bool(x))
print(bool(y))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print('----------')
#an example
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#functions that returns a Boolean Value
def myF():
   return True

print(myF()) #print an answer of the function
print('++++++++')

def myFn():
   return True
if myFn():
   print('Yes') #print Yes if the function return True.
else:
   print('No') #print No if the function return No.

print('^^^^^^^^^^^^')
U = 7000
print(isinstance(U, int))#check data type if object is an integer or not.
#isinstance() fucntion return boolean value.