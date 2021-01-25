#PY4E Assignment 10.2 Solution - Evan Dieterich
'''
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if line.startswith("From "):
        time = line.split()[5].split(":")
        counts[time[0]] = counts.get(time[0],0) + 1
        
hour_count = list()
        
for k,v in counts.items():
    hour_count.append((k,v))
    
hour_count.sort()

for i,j in hour_count:
    print(i,j)
    
