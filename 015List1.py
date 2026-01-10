#List, Tuple, Set, Dictionary = built-in data types in Python.

#List
thelist1 = ["morning", "afternoon", "evening", "night"] #str
thelist2 = [4, 5, 6, 9, 8, 7] #int
thelist3 = [True, False, True, False] #boolean
print(thelist1)
print(len(thelist1))#len() function used to count items in a list
print(thelist2)
print(len(thelist2))
thelist4 = ["KFC", 59, True, "Seven-Eleven"]
print(type(thelist4))

#list() constructor
thelist5 = list(("dog", "cat", "chicken", "duck")) #double round-brackets
print(thelist5)

#list: ordered - changeable, allows duplicate members.
#tuple: ordered - unchangeable, allows duplicate members.
#set: unordered - unchangeable, unindexed - no duplicate members.
#dictionary: ordered - changeable, no duplicate members.

#access items
print("#3 in The list 2 = ", thelist2[2])

#negative indexing
#-1 : last item
#-2 : second from last item

print("The last item of The list 5 = ", (thelist5[-1]))
print(thelist2[2:5]) #specify a range of indexes by specifying where to start and where to end the range.
#5 = end point (not included)
print(thelist5[:2]) #from beginning of the list specify where to end.
print(thelist5[1:]) #specify where to start and end at the last of the list.

list1 = ["dog", "cat", "chicken", "duck", "tiger", "lion", "bird", "butterfly"]
print(list1[-4:-1]) #negative indexes

#check if item exists
if "duck" in list1:
    print("Yes, 'lion' is in the list.")

#Change list items
print(list1)
list1[3] = "worm" #change item value.
print(list1)
list1[4:6] = ["fish", "shark"] #change a range of item values.
print(list1)
list1[2:7] = ["elephant"]
print(list1)

#Insert items
list2 = ["dog", "cat", "chicken", "duck", "tiger", "lion", "bird", "butterfly"]
print(list2)
list2.insert(5, "elephant") #insert() insert a new list item without replacing any of the existing values
print(list2)

#Add list items

#append() : add an item to the end of the list
list3 = ["dog", "cat", "chicken", "duck", "tiger", "lion", "bird", "butterfly"]
list3.append("elephant")
print(list3)
#extend() : append from another list to the current list.
list4 = ("worm", "shark", "fish")
list3.extend(list4)
print(list3)

#add any iterable
list3 = ["dog", "cat", "chicken", "duck", "tiger", "lion", "bird", "butterfly"]
tuple1 = ("fisht", "shark")
list3.extend(tuple1)
print(list3)

