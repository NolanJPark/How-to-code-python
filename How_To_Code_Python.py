from math import *
import random #random is different from math so must be imported seperately
import Python_M_Tools
from Student import Student
from Chef import Chef
from ChineseChef import ChineseChef
from ItalianChef import ItalianChef



#Printing
print("\n\n")
print(300)
print("Hello world")
print("\\': single quote")
print("\\\\: double quote")
print("\\\\: backslash")
print("\\n: new line")
print("\\r: carriage return (everything after is put at the beginning of the line replacing what was there before)")
print("\\t: horizontal tab")
print("\\v: vertical tab")
print("\\b: backspace (when put anywhere but the beginning or end of a print statement it removes the character before it)")
print("\\f: form feed (\\n but for pages instead of lines")
print("\\ooo: octal value (o represents an integer on the ASCII table under oct)")
print("\\xhh: Hex value (same as octal value but hex instead of oct, number goes after x like x45)")
print("0.032805 rounded to 4 decimals is",round(0.032875, 4)) #round(num, int) rounds num normally to fit int decimals
print("\n\n")



#Variables & Arithmetic
x = 1.05
x = "Hello World"
y = 5/2
a = b = c = 5 #all three are set to 5
name = "Nolan"
age = 34
boolean = False
"""
in python variables can equal anything and change 
to anything anytime, the only limiter is potential errors
that could happen when those variables are called
"""
print("x =",x,"\ny =",y)
"""
A "," is used to print number variables but puts
a space in the output, also works for string variables
A "+" is used for string variables but doesn't work
for number variables
"""
print("Hello "+name+" age",age)
print("y to the power of 3 is",pow(y,3),"=",y**3) #pow(num, value raised by) also can be noted as num**raise
print(round(3.4))
print(round(3.5)) #round(num) rounds normally
    #Math that needs math import \/
print(floor(3.7)) #floor(num) basically removes the decimal and leaves an int
print(ceil(3.7)) #ceil(num) if decimal exists remove it and add 1
print(sqrt(3.7)) #sqrt(num) square roots variable
print("Random number between 1 and 10:",random.randint(1, 10)) #returns a random in range inclusive
print("\n\n")



#Strings
str1 = "Programming Time"
str2 = "four"
print(str1.lower()) #string.lower() makes all characters lower case if applicable
print(str1.upper()) #string.upper() makes all characters upper case if applicable
print(str1.isupper()) #string.isupper() returns boolean depending if string is all uppercase or not
print(str1.lower().islower()) #both lower and islower can be used together like so
print(len(str2)) #len(string) return length of string as an int
print(str1[12]) #string[index] returns character at index, neative goes round to the end with -1 being last character
print(str1.index("T")) #string.index("string") returns the index of the string, doesn't do -1 if not existing
print(str1.index("Time"))
print(str1.replace("Times", "Fun")) #string.replace("string1", "string2") replaces string1 with string2, does nothing if string1 isn't found
print(str1.split()) #string.split() returns list of strings that were seperated with spaces
print(str1[12 :]) #string[index : ] returns string of everything after index inclusive
print(str1[0 : 6]) #string[index : length] return string between index and length inclusive
print(str1[0 : 10 : 2]) #string[index : length : num] returns normally but with every num character after the first in the range
print("\n\n")



#Input
name = input("What's you're name ") 
age = input("How old are you? ")
print("Hello "+name+" age",age)
print("\n\n")



#Lists (arrays)
list = [1, 2, 3, 4, 5] #Lists are mutable sequences meaning they can be manipulated
print(list)
print(list[0])
print(list[-3]) #list[index] index can be negative and it loops around with the last thing in the list being -1
print(list[1 : 4]) #list[index : length] returns a list derived from the list between index and length inclusive
list[2] = 7 #list[index] = value, changes value of list at index, if index to high causes error, can be negative
print(list)
otherNums = [12, 43, 23]
list.extend(otherNums) #list1.extend(list2) adds list2 to the end of list1, also works ass list1 + list2
print(list)
otherNums = ["hello", 23, True] #lists may contain mixed variable types
list.extend(otherNums)
print(list)
list.append("fifty three") #list.append(variable) adds variable to the end of list
print(list)
list.insert(2, False) #list.insert(index, variable) adds variable at index and moves everything else in the list up
print(list)
list.remove("hello") #list.remove(variable) removes variable from list, if it doesn't exist it causes an error
print(list)
list.pop() #list.pop() removes top variable in list
print(list)
print(list.index(False)) #list.index(variable) returns index of variable, causes error if variable isn't in list
list.reverse() #list.reverse() reeverses everything in list
print(list)
list.sort() #list.sort() sorts list can only sort ints or strings not both
print(list)
list2 = list.copy() #list.copy() returns a copy of list
print(list2)
list.clear() #list.clear() clears list
print(list)
print("\n\n")



#Tuples (arrayLists)
tuple = (4, 5, 6, 3) #Tuples are immutable and just like lists can contain mixed varible types
print(tuple[1]) #tuple[index] index can be negative and it loops around with the last thing in the list being -1
print(tuple)
print(max(tuple)) #max(tuple) returns greatest value in tuple, doesn't work if tuple contains non-num values
tuple2 = [(3, 2, 12), (5, 1, 3), (19, 23, 4, 98)]
print(min(tuple2)) #min(tuple) returns lowest value in tuple, in a list of tuples it returns the first in the list
print(tuple2)
print(tuple2[2])
print("\n\n")



#Functions
def sayHi(age): # def name(parameters)
    name = input("What's your name? ")
    print("Hello "+name+" age",age)
def cube(num):
    return num*num*num
age = 18
sayHi(age)
print (cube(4))
print("\n\n")



#If Statements
is_male = True
is_Tall = True
if is_male: #In python () isn't necessary for i or else if statments
    gender = "Y"
else:
    gender = "X"
if is_Tall and gender.__eq__("X"): #and, or, and not must be written
    print("You're a tall girl")
elif is_Tall and gender.__eq__("Y"): #elif = else if, & string1.__eq__(string2) returns whether or not they strings are the same case sensitive
    print("You're a tall dude")
elif not is_Tall:
    print("You're not tall")
if gender.__eq__("X") or gender.__eq__("Y"):
    print("You're a person")
else:
    print("How'd you get on this computer?")
x = 34
y = 2
z = 1.7
if z == y:
    print("1.7 equals 2")
elif z == 1:
    print("1.7 equals 1")
else:
    print("1.7 isn't equal to 2 or 1")
if x >= y and z < y:
    print("34 is greater than or equal to 2 and 2 is greater than 1.7")
print("\n\n")



#Dictionaries
abriv = {
    "Lb" : "pounds", #variable1 : variable2,
    "Qt" : "quarts",
    "Kg" : "kilogram"
}
print("I weigh 160 "+abriv["Lb"]) #returns variable 2
print("I have 50 "+abriv.get("Qt")+" of peanut butter") #same as just using abrive[]
print(abriv.get("btw", "Not valid")) #dictionary.get(string, catch) adding the , and catch error traps the get
print("\n\n")



#Loops
x = 1
while x <= 10: #while condition, no () required
    print(x," ")
    x += 1 #Python doesn't let you use ++ but += -= and such is allowed
print()
for letter in "Hello": #for i variable in value
    print(letter)
print()
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)
print()
for i in range(10): #closest to a normal for loop, range is an index with length in ()
    print(i)
print("\n\n")



#2D Lists & Nested Loops
nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
] #2D List with 4 rows and 3 columns
for row in nums: #prints out each row
    print(row)
for row in nums: #prints out each number in nums
    for col in row:
        print(col)
print("\n\n")



#Try/Except
try:
    number = int(input("Enter a number: ")) #usually if you entered a atring it would cuase an error
except:
    print("Invalid") #with except though, the error will be caught

try:
    value = 10 / int(input("Enter another number: "))
except ZeroDivisionError as err: #specifies an error where you divided by 0, and as err sets err to a string explaing the error
    print(err)
except ValueError: #specifies an error where the values where incorrect
    print("Invalid input")
"""
ImportError: imported module isn't found
IndexError: index is out of range
KeyError: key isn't found in dictionary
KeyboardInterrupt: user hits interrupt keys Ctrl+C or Delete
MemoryError: operation ran out of memory
NameError: variable name isn't found in local or global scope
OverflowError: arithmetic operation is to large
RuntimeError: error doesn't apply to any other category
SyntaxError: syntax error is encountered
ValueError: value doesn't match type
ZeroDivisionError: you tried to divide by zero
"""
print("\n\n")



#Reading Files
employee_file = open("How_To_Code_Python_Text_File.txt", "r") #open("text file name", opening mode) opens file under employee_file
"""
Opening Methods:
    Read Only ("r"): opens file for reading, no file creates an I/O error
    Read and Write ("r+"/"w+"): opens file for reading and writing, over-writes starting at the beginning of the file
    Write Only ("w"): opens file for writing, data is over-written starting at the beginning and will create file if it doesn't exist
    Append Only ("a"): opens file for writing, adding data to the end after existing data
    Append and Read ("a+"): opens file for reading and writing, data is added to the end of existing data and will create an file if it doesn't exist
"""
print(employee_file.readline()) #reading starts at the beginning of the file and goes through it, readlines also creates an extra line
print(employee_file.readline()) #since the first line has already been read the nest line in the file will be output
print(employee_file.readline()[1])
print(employee_file.readline()[1]) #while this is the same statment as the previous one they'll both output different things due to how read works
print(employee_file.read()) #variable.read() outputs entire file not yet read
employee_file.close() #variable.close() closes file to protect against problems
print("\n")
employee_file = open("How_To_Code_Python_Text_File.txt", "r") #you can open files again and read from the beginning again
for employee in employee_file.readlines():
    print(employee) #readline() will print two lines after the line
    print("|")
employee_file.close()
print("\n\n")



#Writing into Files
x = input("Would you like to reset the file(1) or append it (2)")
if x.__eq__("1"):
    employee_file = open("How_To_Code_Python_Text_File.txt", "w") #write basically wipes the file and rewrites it
    employee_file.write("Jim - Salesman\nDwight - Salesman\nPam - Receptionist\nMichael - Manager\nOscar - Accountant")
    employee_file.close()
elif x.__eq__("2"):
    employee_file = open("How_To_Code_Python_Text_File.txt", "a") #append adds to the end of file
    employee_file.write("\nToby - Human Resources")
    employee_file.close()
print("\n\n")



#Modules &  Pip
print("Roll the dice:",Python_M_Tools.roll_dice())
print("120 meters is",round(Python_M_Tools.convert_m_to_mi(12), 4),"miles")
print("\n\n")



#Classes and Objects
student1 = Student("Jim", "Business", 3.1, False) #called constructor
student2 = Student("Pam", "Artist", 2.5, True) #you can make multiple variables representing classes
print(student1.name)
print(student2.gpa)
student1.check()
student2.check()
print(student1.name + " on the honor roll:", student1.honor_roll())
print(student2.name + " on the honor roll:", student2.honor_roll())
print("\n\n")



#Inheritance
myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice()

myItalianChef = ItalianChef()
myItalianChef.make_chicken()