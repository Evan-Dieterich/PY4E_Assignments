#PY4E Assignment 9.4 Solution - Evan Dieterich
'''
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
    
fh = open(name)
sendcounts = dict()
senders = list()
for line in fh:
    record = line.split()
    if "From" not in record: continue
    else:
        senders.append(record[1])

for i in senders:
    sendcounts[i] = sendcounts.get(i, 0) + 1
    
maxkey = 0
maxval = 0
    
for key,val in sendcounts.items():
    if val > maxval:
        maxval = val
        maxkey = key
        
print(maxkey, maxval)
