#remove list items

list1 = ["dog", "cat", "tiger", "chicken", "duck", "tiger", "lion", "bird", "butterfly"]
print(list1)
list1.remove("chicken") #remove() : removes the specified item.
print(list1)
list1.remove("tiger") #remove the first occurrence of "tiger"
print(list1)
list1.pop(4) #remove specified index.
print(list1)
list1.pop() #remove the last item, do not specify the index.
print(list1)
del list1[1] #del = keyword = also removes the specified index.
print(list1)
del list1 #del etire list.
#print(list1) #it doesn't display anything.
list1 = ["dog", "cat", "chicken", "duck", "tiger", "lion", "bird", "butterfly"]
list1.clear() #clear() : clear the list
#The list still remains, but it has no comtent.
print(list1)

#Loop lists
list1 = ["dog", "cat", "chicken", "duck", "tiger", "lion", "bird", "butterfly"]
for D in list1: #loop through the list items : "for" loop
    print(D) #print all items in the list, line by line.

#loop through the index numbers.
list2 = ["dog", "cat", "chicken"]
for D in range(len(list2)): #loop through the list items by referring to their index number.
    print(list2) #print all items by referring to their index number.
print("---------")
B = 0
while B < len(list1): #to increase the index by 1 after each iteration.
    print(list1) #print all items, using a while loop to go through all the index numbers.
    B += 1 #stop loop if B >= len(list1)

#looping using list comprehension
[print(g) for g in list1] #short syntax for loop

#list comprehension
list1 = ["dog", "cat", "tiger", "chicken", "duck", "tiger", "lion", "bird", "butterfly"]
list_new = [] #create a new list based on the values of an existing list


for X in list1:
    if "i" in X:
        list_new.append(X)

print(list_new)

#list comprehension : in only one line of code
new_list = [Y for Y in list1 if "o" in Y]
print(new_list)

#Syntax
#newlist = [expression for item in iterable if condition == True]
#The return value is a new list, leaving the old list unchanged.
#Condition a filter that only accepts the items that evaluate to True.
new_list = [x for x in list1 if x != "lion"]
print(new_list) #if x != "lion" will return True for all elements other than "lion" and making the new list comtain all list1 except "lion".
new_list = [x for x in list1]

NewList = [z for z in range(10)]
print(NewList)

NewList = [z for z in range(10) if z < 4]
print(NewList)

print("00000000000")
#Expression
oldlist = ["dog", "cat", "tiger", "chicken", "duck", "tiger", "lion", "bird", "butterfly"]
print(oldlist)
NewList = [x.upper() for x in oldlist]
print(NewList)
NewList = ['Hey!' for o in oldlist]
print(NewList)
NewList = [n if n != "cat" else "dog" for n in oldlist]
#return "dog" instead of "cat".
print(NewList)

#Sort list alphanumerically
#sort()

#Ascending
list1 = ["dog", "cat", "tiger", "chicken", "duck", "tiger", "lion", "bird", "butterfly"]
list1.sort() #sort the list alphabetically.
print(list1)
list2 = [234, 123, 6, 42, 9, 84]
list2.sort() #sort the list numerically.
print(list2)

#Deascending
list1.sort(reverse = True)
print(list1)
list2.sort(reverse = True)
print(list2)

#Customize sort function
#key = function
def func(n):
    return abs(n- 66) #sort the list based on how close the number is to 66.

list2.sort(key = func)
print(list2)

list3 = ['Shark', 'shrimp', 'Lion', 'Ant', 'bird', 'cat', 'Tiger']
list3.sort() #case sensitive sort result.
print(list3)
list3.sort(key = str.lower) #case insensitive sort result.
print(list3)
list3.reverse()
print(list3)

list3 = ['Shark', 'shrimp', 'Lion', 'Ant', 'bird', 'cat', 'Tiger']
list3.sort(reverse = True)
print(list3)

