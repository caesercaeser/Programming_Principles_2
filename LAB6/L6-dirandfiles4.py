import os
with open('C:/labs/pp2/LAB6/examplefile.txt', 'r') as file:
    x = sum(1 for line in file)
print(x)
