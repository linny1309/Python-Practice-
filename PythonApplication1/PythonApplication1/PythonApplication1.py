
import random
import sys
import os

print("Hello World")

name = "Derek"
print(name)

#Comment

'''
Multiline Quote
'''

#Operations, Math

print("5 + 2 =",5+2)
print("5 - 2 =",5-2)
print("5 * 2 =",5*2)
print("5 / 2 = ",5/2)
print("5 ** 2 =",5**2)
print("5 % 2 = ",5%2)
print("5 // 2 = ",5//2)

print("1 + 2 - 3 * 2 =", 1+2-3*2)
print("(1 + 2 - 3) * 2 =", (1+2-3)*2)

quote = "\"This is the first part,"

multi_line_quote = ''' and this is
for the second multi-line part"'''

new_string = quote + multi_line_quote

print("I know that,", new_string)
print("I do not like ", end="")
print("new lines")

grocery_list = ['Apple','Bananas','Cukes']
print('First Item: ',grocery_list[0])

grocery_list[0] = 'Gala Apple'
print('First Item: ',grocery_list[0])

other_events = ['Wash Car', 'Pick Up Kids']

to_do_list = [other_events, grocery_list]
print(to_do_list)
print((to_do_list[1][0]))

grocery_list.append('Butter')

print(grocery_list)

grocery_list.insert(1, "Pickle")

grocery_list.remove("Pickle")

grocery_list.sort()

print(grocery_list)

to_do_list2 = other_events + grocery_list

print(len(to_do_list)) #length of list
print(len(to_do_list[1]))
print(max(to_do_list)) #max of list, in case of string it is alphabetically determined
print(min(to_do_list))

pi_tuple = (3,1,4,1,5,9) #Like a list but cannot be modified after creation

new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

#print(len(tuple))
#print(min(tuple))
#print(max(tuple))

#dictionary

starwars_chars = {'Han Solo' : 'Smuggler', 
                  'Luke Skywalker' : 'Jedi',
                  'Chewie' : 'Wookie'}

print(starwars_chars['Han Solo'])
#del starwars_chars['Han Solo']
print(len(starwars_chars))
print(starwars_chars.get("Chewie"))
print(starwars_chars.keys())
print(starwars_chars.values())

#if else elif (else if) conditional statements

age = 21

if age > 16 :
    print('You are old enough to drive')
else :
    print('You not old enough to driver')
if age >= 21 :
    print('You can drink and drive')
elif age >= 16 :
    print('You can drive but not drink')
else :
    print('You cant drink and drive')

#and or not logical operators 

if((age >= 1) and (age <= 17)):
    print("you are a minor")

#loop

for x in range(0, 10): #until 10 not including 10
    print(x, ' ', end="")

print('\n')

for y in grocery_list: #in the list
    print(y)

for x in[2,4,6,8,10]:
    print(x)

tri_list = [[1,2,3],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range(0,3):
        print(tri_list[x][y])

random_num = random.randrange(0,100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)

i = 0;

while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        break
    else:
        i += 1;
        continue;

    i += 1 

#methods/functions

def addNumber(fnum, lnum):
    sumNum= fnum + lnum
    return sumNum

print(addNumber(1,4))

#functions getting input

print('what is your name')

yourname = sys.stdin.readline()

print('Hello', yourname)

#string concat

sentance = "go to the garage"

print(sentance[0:2]) #first two chars

print(sentance[-6:]) #last 5 

print(sentance[:-6]) #up until last 5

print("%c is my %s letter and my number %d number is %.5f" % ("X", 'favorite', 1, 0.14))

#Manipulating strings 

long_string = "I'll catch you if you fall - The Floor"

print(long_string.capitalize())

print(long_string.find("Floor"))

print(long_string.isalpha())

print(long_string.isalnum())

print(long_string.replace("Floor", "Ground"))

print(long_string.strip()) #split white space

quote_list = long_string.split(" ")

print(quote_list)

#file input output

class Animal:
    __name=""
    __height=0
    __weight=0
    __sound=0

    def __init__(self,name,height,weight,sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Dog(Animal): #Inheritance 
    __owner = ""

'''
test_file("test.text", "wb")
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("Write me to the file\n","UTF-8"))
test_file.close()
test_file = open("test.txt","r+")
text_in_file = test_file.read()
print(tet_in_file)
os.remove("test.txt")
'''













