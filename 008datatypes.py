#text type: str
#numeric types: int, float, complex
#sequence types: list, tuple, range
#mapping type: dict
#set types: set, frozenset
#boolean type: bool
#binary types: bytes, bytearray, memoryview
#none type: NoneType

#to display the type of the variable.
a=2 #int
print(a)
print(type(a)) #getting the data type,

#list
b=['cat','dog','bird','fish','snake','tiger','lion']
#tuple
c=('cat','dog','bird','fish','snake','tiger','lion')
print(b)
print(type(b))
print(c)
print(type(c))


#setting the data type
d = {"name" : "John", "age" : 36}
print(d)
print(type(d))

#setting the specific data type
e = dict(name="John", age=36)
print(e)
print(type(e))

f = True
print(f)
print(type(f))
