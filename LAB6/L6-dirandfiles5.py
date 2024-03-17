import os
list = list(input().split())
with open('C:/labs/pp2/LAB6/examplefile.txt', 'w') as file:
    for i in list:
        file.write(str(i) + ' ')
