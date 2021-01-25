#PY4E Assignment 2 Solution - Evan Dieterich
#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.

hrs = input("Enter Hours: ")
rate = input("Enter pay rate: ")
rate = float(rate)
hrs = float(hrs)
grossPay = (hrs * rate)
print("Pay:", grossPay)
