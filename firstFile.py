
import random
import sys
import os

# comment
'''
multiline comment
num= 5

Datatypes
String 
Numbers
Lists 
Tuples 
Dictionaries

variables starts with letter can have numbers or underscores

+ - * / % 
** exp
//  divide and throw out remainder


'''
x= "this is a varialbe"

print(x)

x = "this is the changed value"

print(x)

myVariable = "this is a string" + " with text added"

print(myVariable)
my_num = 2
my_num = my_num +27
htmStr = "<html><head><title>Just created this " + str(my_num) + "file with this title</title></head></html>"
my_html_file = open("/C-Drive-Documents/aa UBS/Python/pythonBeginners/my_html.html", "w")
my_html_file.write(htmStr)
my_html_file.close()

print("5 // 2 = ", 5//2)
print("5**2 =", 5**2)

quote = "\"qwote character at start "
print(quote)
multilineString = '''here is a multi
line string so it works just fine
like 

this'''
print(multilineString)

print("%s %s %s" % ('I like the quote of ', quote, multilineString) )

print('print newline *5 \n'  *5)








