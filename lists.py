import random
import sys
import os

grocery_list = ['apples', 'oranges', 'x[rprotein bars', 'cantelope']

print(grocery_list[0])

grocery_list[0] = "green apples"

print(grocery_list[0:2])

other_events = ['mothers day', 'move furniture']

combineList = [grocery_list, other_events]

print(combineList)

print(combineList[1][0])

combineList2 = grocery_list
combineList2.append(other_events[0])
combineList2.append(other_events[1])
print(combineList2)

other_events.insert(1, 'pickle')
print(other_events)
other_events.sort()
print(other_events)
other_events.reverse()
print(other_events)

print("grocery_list =", grocery_list)
print("other_events =", other_events)
print("combineList= ", combineList)
print("min(combineList)= ", min(combineList))
print("max(combineList)= ", max(combineList))
print("len(combineList)= ", len(combineList))