import numpy as np

number1 = int(input("Enter Number 1: "))
number2 = int(input("Enter Number 2: "))

array1 = np.array(number1)
array2 = np.array(number2)

addsub = (input("Enter + for Addition or - for Subtraction: "))

if addsub == "+":
    add = array1 + array2
    print("Result: ",add)
elif addsub == "-":
    sub = array1 - array2
    print("Result: ",sub)