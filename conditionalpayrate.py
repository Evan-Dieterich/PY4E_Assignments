#PY4E Assignment 3.1 Solution - Evan Dieterich
'''
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
'''

hrs = input("Enter Hours:")
rate = input("Enter rate:")
h = float(hrs)
r = float(rate)

if(h > 40):
    h -= 40
    grossPay=(h *(r * 1.5) + (40 * r))
    print(grossPay)
else:
    print(h*r)
