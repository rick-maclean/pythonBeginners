import random
import sys
import os

test_file = open("test.txt", "wb")
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("Write me to the file oh ya\n", 'UTF-8'))
test_file.close()

test2_file = open("test.txt", "r+")
text_in_file = test2_file.read()

print(text_in_file)

test2_file.close()
#os.remove("test.txt")