#logical operators
#used to combine conditional statements
#and, or, not
x = 7
print(x > 0 and x < 10)
print(x < 7 or x > 10)
print(not(x > 3 and x < 10)) #reverse result
print('--------------')

#identity operators
#Used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
#is, is not
x = ["lion", "tiger", "sneak"]
y = ["lion", "tiger", "sneak"]
print(x is not y)
#is: check if both variables point to the same object in memory.
#==: check if the values of both variables are equal.
x = [3, 2, 1]
y = [3, 2, 1]
print(x == y)
print(x is y)
print(x is x)
print([3, 2, 1] is [3, 2, 1])

#membership operators
#Used to test if a sequence is presented in an object.
#in, not in
animals = ['dog', 'cat', 'bird', 'lion', 'tiger', 'sneak', 'elephant']
print('sneak' in animals)
print('walrus' in animals)
print('butterfly' not in animals)
#membership operators also work with str.
py = 'Specification changes during implementation.'
print('s' in py)
print('H' in py)
print('h' in py)
print('T' in py)

#bitwise operators
#Used to compare binary numbers.
#&, |, ^, -, <<, >>
print(4 & 3)
print(4 | 3)
print(4 ^ 3)

#operator precedence
#describes the order in which operations are performed.
print((4+8) - (2+4))
print(70 + 5 * 6) #* has higher precedence than +
