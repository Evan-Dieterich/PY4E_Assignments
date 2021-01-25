#PY4E Assignment 4.6 Solution - Evan Dieterich
'''
Write a function to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
'''

def computepay(h,r):
    if h > 40:
        h -= 40
        pay = (h * (1.5 * r) + (40 * r))
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h,r)
print("Pay",p)
