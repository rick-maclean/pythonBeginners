import random
import sys
import os

# if else elif == != > >= <=

age = 7

if age > 16 :
    print('you are over 16')
else :
    print('you are 16 or under')

# logical operators    and   or   not   

if ((age >=1) and (age<=18)):
    print("age >=1 and <=18")
elif (age ==21) or (age>=65):
    print ("you blah blah blah")
elif not(age==30):
    print("age == 30")
else:
    print("this is the else part")