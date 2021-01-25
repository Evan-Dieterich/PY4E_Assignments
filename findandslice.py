#PY4E Assignment 6.5 Solution - Evan Dieterich
'''
Write code using find() and string slicing to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.
'''

text = "X-DSPAM-Confidence:    0.8475";
numpos = text.find(".")

num = text[numpos:]
num = float(num)
print(num)
