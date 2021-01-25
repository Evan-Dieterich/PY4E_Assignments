#PY4E Assignment 7.2 Solution - Evan Dieterich

'''
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values
'''

confidence = 0
confidencecount = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count += 1
    perpos = line.find(".")
    confidence = line[perpos:]
    confidence = float(confidence)
    confidencecount += confidence
    
avg = confidencecount/count
print("Average spam confidence:", avg)
