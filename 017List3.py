#Copy lists
#copy() method
print('--------copy-list---------')
mylist = ['cat', 'dog', 'tiger', 'shark', 'bird', 'horse', 'duck', 'chicken', 'ape', 'monkey']
yourlist = mylist.copy()
print(yourlist)
print(mylist)
#list() method
yourlist = list(mylist)
print(yourlist)
#slice operator
yourlist = mylist[:] #make a copy a list with the : operator
print(yourlist)

print('------join-lists------')
#Join lists
#+ operator : easiest ways
mylist = ['cat', 'dog', 'tiger', 'shark', 'bird', 'horse']
yourlist = ['duck', 'chicken', 'ape', 'monkey', 'fish', 'elephant']
ourlist = mylist + yourlist
print(ourlist)

#append list2 into list1
list1 = ['cat', 'dog', 'tiger', 'shark', 'bird', 'horse']
list2 = ['duck', 'chicken', 'ape', 'monkey', 'fish', 'elephant']
for g in list2:
    list1.append(g)

print (list1)

#extend() method
list1 = ['cat', 'dog', 'tiger', 'shark']
list2 = [0, 1, 2, 3]
list1.extend(list2)
print(list1)

