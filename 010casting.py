x = float(66)
print(x)

#strings
print("It's walking on the moon.")

a = "It's walking on the moon."
print (a)

#multiline string
b = """It's walking on the moon
since yesterday."""
print(b)

print(a[13]) #get the character at position 13

for b in "Jack": #loop through the letters in the word "Jack"
    print (b)

print(len(a)) #Get the length of a string, use the len() function.

print("moon" in a) #Use keyword "in" to check if the word "moon" is present in the string.

if "walk" in a: #check string use an 'if' statement.
    print("yes, 'walk' is present.")
else:
    print("no, 'walk' is not present.")

#check if not, use "not in"
print("sun" not in a)

if "sun" not in a:
    print("No, 'sun' is not present.")


