#Operators are used to perform operations on variables and values.

#+ operator to add together values, and it can also add a variable and a value together.
print(6+9)

a = 9+8
b = a+7
c = b+b
d = a+b+c
print(a)
print(b)
print(c)
print(d)
print('++++++++++++')
print(a**2)
print(a*b)
print(d/a)
print(c//b)
print(b%c)
print(c-d)
print('++++++++++++++')
x = 2
y = 8
print(y / x)
print(y // x)
print(y % x)

#Assignment operators
x=2
x+=3
print(x)
x|=3
print(x)
x|=6
print(x)


#The Walrus Operators
numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#*****I need to learn more about := (Walrus Operator)

#comparison operators
x = 3
y = 8

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x <= y)
print(x >= y)

#chaining comparison operators
print(1 < x <10)
print(1 < x and x <10)
