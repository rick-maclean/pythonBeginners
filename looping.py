import random
import sys
import os

# for x = 0 but not 10,  end="" does not print newLines
for x in range(0, 10):
    print(x, ' ', end="")

print('\n') 
print('Grocery List to be printed next')

grocery_list = ['apples', 'oranges', 'x[rprotein bars', 'cantelope']

for y in grocery_list:
    print(y)

for x in [2,4,6,8,17]:
    print(x)

print()
print("now printing num_list nested loops")
num_list= [[1,3,5], [10,20,30], [5,10,35]]

for x in range(0, 3):
    for y in range(0,3):
        print(num_list[x][y])


print()
print('doing while loop with random numbers')
random_num = random.randrange(0,100)
while(random_num !=15):
    print(random_num)
    random_num = random.randrange(0,30)

i=0
while (i <=20):
    if(i%2 == 0):
        print(i)
    elif(i==9):
        break
    else:
        i += 1
        continue
    i = i+1



