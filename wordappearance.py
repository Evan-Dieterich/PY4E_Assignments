#PY4E Assignment 8.4 Solution - Evan Dieterich
'''
Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() method. 
The program should build a list of words. 
For each word on each line check to see if the word is already in the list and if not append it to the list.
'''

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    fhlist = line.rstrip().split()
    for word in fhlist:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)
