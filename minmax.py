#PY4E Assignment 5.2 Solution - Evan Dieterich
'''
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers.
'''

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num = float(num)
    except:
        print("Invalid input")
    else:
        if smallest is None: #first number!
            smallest = num
            largest = int(num)
        elif num < smallest:
            smallest = int(num)
        elif num > largest:
            largest = int(num)
print("Maximum is", largest)
print("Minimum is", smallest)
