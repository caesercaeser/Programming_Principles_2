import os
with open('C:/labs/pp2/LAB6/examplefile.txt', 'r') as r:
    with open('C:/labs/pp2/LAB6/examplefile_copy.txt', 'w') as w:
        for line in r:
            w.write(line)
