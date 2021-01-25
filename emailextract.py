#PY4E Assignment 8.5 Solution - Evan Dieterich
'''
Open the file mbox-short.txt and read it line by line. 
When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line
'''

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    linelist = line.rstrip()
    if not linelist.startswith("From "): continue
    fromlines = linelist.split()
    print(fromlines[1])
    count += 1
print("There were", count, "lines in the file with From as the first word")
