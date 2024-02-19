
# * Python Arithmetic Operators

# ! Floor division //
x = 15
y = 2

print(x // y)

#the floor division // 
# rounds the result down to the 
# nearest whole number

'''
Exponential operators **

'''
x = 2
y = 5

print(x ** y) #same as 2*2*2*2*2

# * Modules % 
x = 5
y = 2

print(x % y) #1

# * Python Assignment Operators
# ? Assignment operators are used to assign values to variables:

x = 5

x += 3

print(x)

# ! Example
x = 5

x -= 3

print(x)

# ! Example
x = 5

x *= 3

print(x)

# ! Example
x = 5

x /= 3

print(x)

# ! Example
x = 5

x%=3

print(x)

x = 5

x//=3

print(x)

x = 5

x **= 3

print(x)

x = 5

x &= 3

print(x)

# ! Example
x = 5

x |= 3

print(x)

# ! Example
x = 5

x <<= 3

print(x)

# ! Example
x = 5

x >>= 3

print(x)


# * Python Comparison Operators
# !Comparison operators are used to compare two values:

# ! Equal ==

x = 5
y = 3

print(x == y)

# returns False because 5 is not equal to 3
# Not Equal !=
x = 5
y = 3

print(x != y)

# returns True because 5 is not equal to 3

x = 5
y = 3

print(x > y)

# returns True because 5 is greater than 3
x = 5
y = 3

print(x < y)

# returns False because 5 is not less than 3

x = 5
y = 3

print(x >= y)

# returns True because five is greater, or equal, to 3
x = 5
y = 3

print(x <= y)

# returns False because 5 is neither less than or equal to 3

# * Python Logical Operators
# ! Logical operators are used to combine conditional statements:

# ! AND Returns True if both statements are true
x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10
  
  
# * Returns True if one of the statements is true
# ! Example OR

x = 5

print(x > 3 or x < 4)

# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

# Reverse the result, returns False if the result is true
# ! Example NOT

x = 5

print(not(x > 3 and x < 10))

# returns False because not is used to reverse the result


# * Python Identity Operators
'''
Python Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they 
are actually the same object, with the same memory location:

'''
# ! Example is Operator
# Returns True if both variables are the same object

fruity1_ = ["apple", "banana"]
fruity2_ = ["apple", "banana"]
fruity3_ = fruity1_

print(fruity1_ is fruity3_)

# ? returns True because fruity3_ is the same object as fruity1_

print(fruity1_ is fruity2_)

# ? returns False because fruity1_ is not the same object as fruity2_, 
# ? even if they have the same content

print(fruity1_ == fruity2_)

# ? to demonstrate the difference betweeen "is" and "==": 
# ? this comparison returns True because fruity1_ is equal to fruity2_


# ! Example  is not
# Returns True if both variables are not the same object

x1_ = ["apple", "banana"]
y1_ = ["apple", "banana"]
z1_ = x1_

print(x1_ is not z1_)

# returns False because z is the same object as x

print(x1_ is not y1_)

# returns True because x is not the same object as y, 
# even if they have the same content

print(x1_ != y1_)

# to demonstrate the difference betweeen "is not" and "!=": 
# this comparison returns False because x is equal to y


# * Python Membership Operators / TRUTH VALUE TESTING IN PYTHON

# ? Membership operators are used to test 
# ? if a sequence is presented in an object
 
 # ! Operators in (x in y)
#	? Returns True if a sequence with the 
# ? specified value is present in the object

x2_ = ["apple", "banana"]

print("banana" in x2_)

# returns True because a sequence with the value "banana" is in the list

# ! Operator not in (x not in y)
# Returns True if a sequence with the specified value is not present in the object

x3_ = ["apple", "banana"]

print("pineapple" not in x3_)

# returns True because a sequence with the value "pineapple" is not in the list

# * Calculate the area of a Rectangle
# ! 1 create a variable rectangleLength and set it's value to 10
# ! 2 create a variable rectangleBreadth and set it's value to 5
# ! 3 rectangleAngle = rectangleLength * rectangleBreadth
# ! 4 print out the value of rectangleArea

rectangleLength = 10
rectangleBreadth = 5
rectangleArea = rectangleLength * rectangleBreadth
print(rectangleArea)


# * ESCAPE CHARACHTER \
'''
To quote a quote, we need to “escape” it, by preceding it with \. Alternatively, we can use the other type of quotation marks:

'doesn\'t'  # use \' to escape the single quote...
"doesn't"
"doesn't"  # ...or use double quotes instead
"doesn't"
'"Yes," they said.'
'"Yes," they said.'
"\"Yes,\" they said."
'"Yes," they said.'
'"Isn\'t," they said.'
'"Isn\'t," they said.'

'''

s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), special characters are included in the string
'First line.\nSecond line.'
print(s)  # with print(), special characters are interpreted, so \n produces new line
# ? First line.
# ? Second line.

print('C:\some\name')  # here \n means newline!
# ? C:\some
# ? ame
print(r'C:\some\name')  # note the r before the quote
# ? C:\some\name


# * PLACEHOLDER IN PYTHON
# ? using %s as a placeholder to pass a number
myAge = 23
myMessage = ' I am %s years old'
print(myMessage % myAge)


# ! More Examples
# ! Using more than one placeholder in python

myScore = 30
myWins = 'I won the coupon'
myBetting = '%s  with the %s points.'
print(myBetting % (myWins, myScore))


# * Using formated string to make this concise
# ! replacing the placeholder with a curly braceless
myScore1 = 30 + 5
myWins1 = 'I won the coupon'
myBetting1 = f'{myWins1} with a {myScore1} points'
print(myBetting1)

# * To make the code more concise and readable 
# * with formatted string
# ! use the letter f''

myWins2 = 'I won the coupon'
myBetting2 = f'{myWins2} with a {30 + 5} points'
print(myBetting2)


# * STRINGS IN PAYTHON / STRING LITERALS
# ! STRING METHODS IN PYTHON
# ! STRING LITERALS IN PYTHON
# ! STRINGS CONCATENATIONS IN PYTHON
'''
Strings can be concatenated (glued together)
with the + operator, and repeated with *:
'''
# 3 times 'un', followed by 'ium'
word = 3 * 'un' + 'ium'
print(word)
# ? unununium


'''
This feature is particularly useful 
when you want to break long strings:
'''

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

# ! STRING METHODS IN PYTHON
txt1 = 'Welcome to my only world'
print(txt1.capitalize())
print(txt1.count('2'))
print(txt1.count('3'))


txt2 = 'Welcome to my world'
print(txt2.upper())
print(txt2.lower())
print(txt2.index('c'))
print(txt2.index('o'))


txt3 = 'Welcome to my world'
print(txt3.islower())
print(txt3.isupper())
print(txt3.replace('o', 'a')) # use to replace characters or value'


'''
#! Indexing in String
Strings can be indexed (subscripted), with the first character having index 0. 
There is no separate character type; a character is simply a string of size one:
'''

word = 'Python'
print(word[0])  # character in position 0
print(word[5])  # character in position 5

# ! Indices may also be negative numbers, to start counting from the right:
# ! Note that since -0 is the same as 0, negative indices start from -1.

print(word[-1])  # last character
'n'
print(word[-2])  # second-last character
'o'
print(word[-6])
'P'

# STRING SLICING
'''
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing 
allows you to obtain a substring:
'''
word = 'Python'
print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
'Py'
print(word[1:2])
print(word[0:4])
print(word[1:4]) 
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)
'tho'

#! Default and same as above
'''
Slice indices have useful 
defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.

'''
word = 'Python'
print(word[:2]) # same as 0:2  # character from the beginning to position 2 (excluded)
'Py'
print(word[:4])  # same as 0:4
print(word[4:])   # characters from position 4 (included) to the end
'on'
print(word[2:]) 
#thon
print(word[-2:])  # characters from the second-last (included) to the end
'on'
print(word[-4:])

# Create a new string with slicing
'J' + word[1:]
'Jython'
word[:2] + 'py'
'Pypy'


# ! The built-in function len() returns the length of a string:
print(len(word))

s = 'supercali'
print(len(s))


# * LISTING
# ! Lists might contain items of different types, but usually the items all have the same type.

primeNumbers = [2,4,5,7,9]
print(type(primeNumbers)) # list
names = ["Ivy", "Emmy", "Delulu"]
print(type(names)) # list
primeMembersAndNumbers = ['Ivy', 'Emmy', 5, 7]
newList = primeMembersAndNumbers
print(newList)

# ! Like strings LIST CAN BE INDEXED
print(primeNumbers[0]) # 2
print(primeNumbers[-1]) #9
print(primeNumbers[:1]) # [2]
print(primeNumbers[1:]) # [4, 5, 7, 9]
print(primeNumbers[-3:]) # [5, 7, 9]
print(primeNumbers[3:]) # [7, 9]
print(primeNumbers[3:2]) # []
print(primeNumbers[:5]) # [2, 4, 5, 7, 9]

# shallow copy
print(primeNumbers[:])  


# How to use replace in list

cubes = [1, 8, 27, 65, 125]  # something's wrong here
expo = 4 ** 3  # the cube of 4 is 64, not 65!
##print(expo)
# 64
cubes[3] = 64
#print(cubes.replace(4**3)) 
#print(cubes.replace(64))

# = 64  # replace the wrong value
cubes = [1, 8, 27, 64, 125]   

'''
You can also add new items at the end of the list,
by using the list.append() method 
'''
print(cubes.append(216))  # add the cube of 6
print(cubes.append(7 ** 3))  # and the cube of 7
# cubes [1, 8, 27, 64, 125, 216, 343]


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letter = ['Emmy', 'London', 'New York']
#print(letter.replace('Emmy', 'Canada'))
#print(letter.upper())

print(len(letters))
['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
list1Point_ = letters[2:5] #= ['C', 'D', 'E']
print(list1Point_)
#print(letters.replace('e', 'E'))

print(txt3.replace('o', 'a')) # use to replace characters or value'

# Nested List
alphabet1 = ['a', 'b', 'c']
numbers1 = [1, 2, 3]
lis1_ = ['a', 'n']
listings1_ = alphabet1 + numbers1 + lis1_
print(listings1_)
print(len(listings1_))
print(listings1_[4])
print(listings1_[2:2]) # [] empty
print(listings1_[:]) # [] empty


# * Using the if statment for bool truth value
# * if can be use in sequence comparison
'''
 multi-line construct. As an example,
 take a look at this if statement:

'''
the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")

the_moment_of_life = True
if the_moment_of_life:
  print('Life is good')
else:
  print('Life will get better')


the_moment_of_work = False
if the_moment_of_work:
  print('Upskill yourself')
else:
  print('Work life balance')  








  

# Fibonacci series:
#! F0	F1	F2	F3	F4	F5	F6	F7	F8	F9	F10	F11	F12	F13	F14	F15	F16	F17	F18	F19
#! 0	1	1	2	3	5	8	13	21	34	55	89	144	233	377	610	987	1597	2584	4181


'''
#! The while loop executes as long as 
the condition (here: a < 10) remains true.

'''
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

'''
The first line contains a multiple assignment: the variables a and b simultaneously get the new values 0 and 1. On the last line this is used again, demonstrating that the expressions on the right-hand side are all evaluated first before any of the 
assignments take place. The right-hand side expressions are evaluated from the left to the right.
'''

'''
#! using the keyword end
The keyword argument end can be used to avoid 
the newline after the output, or end the output with a different string:

'''
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b    