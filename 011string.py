x = "I walks under the sea every day."
print(x)

#slice syntax
print(x[7:17]) #Specify range of characters position, the start is 7 and the end 16.
print(x[:3]) #From start to position 2.
print(x[23:]) #From position 23 to the end.
print(x[-6:-1]) #Negative indexing.

#modify strings
#built-in methods
print(x.upper()) #under() method to returns the string in upper-case.
print(x.lower()) #lower() method to returns the string in lower_case.

y = " I walks under the sea every day. "
print(y.strip()) #strip() method to removes the whitespace before or after actual text.
print(y.replace('w', 't')) #replace() method to replace any letters to the existing letters.
print(y.split(' '))#split() method to separates words from string and become to list.

#Concatenation
a=x
b='I know how to walk in the air.'
c=a+' '+b
print(c)

#string format
x = 'I am'
y = 24
z = 'years old.'
a = (f'I am {y} years old.')
#cannot combine strings and numbers
#F-strings
#f in front of the string literal and add curly brackets "{}" for variables.
print(a)

#place holders
#can contain variables, operations, functions, and modifiers to format the value.
x = 24
y = f"I am {x} years old."
print(y)
x = 34
y = f"I am {x:.2f} years old."
#Display 2 decimals with :.2f
print(y)

y = f"I am {x-10} years old."
#placeholder: math operation
print(y)

#escape character
x = "\tCoding, or programming, is the process of \nwriting instructions \"code\" in a specific language\n that computers understand to perform tasks,\n build software, create websites, and power apps,\n essentially acting as a translator to tell machines\n what to do, from simple actions to\n complex operations."
#\t for tab, \n for new line, \" or \' for fix quote trouble in str.
print(x)