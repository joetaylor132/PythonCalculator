#a calculator programme

import time

def StartUp():
    print ("Welcome to my calculator application")
    print ("Made by Joe Taylor")
    print ("Version 1.0 - 2/12/18")
        
def MainMenu():
    print (" ")
    print ("1. Addition")
    print ("2. Subtraction")
    print ("3. Division")
    print ("4. Multiplication")
    
StartUp()
while True:
    time.sleep(2)
    MainMenu()
    
    Menuchoice = int(input("enter the number of your choice: "))
    if Menuchoice == 1:
        print ("Addition - add numbers..")
        add1 = int(input("Enter your first number: "))
        add2 = int(input("Enter your second number: "))
        addans = add1 + add2
        print ("The answer is ", addans)
    elif Menuchoice == 2:
        print ("Subtraction - take away numbers..")
        sub1 = int(input("Enter your first number: "))
        sub2 = int(input("Enter your second number: "))
        subans = sub1 - sub2
        print ("The answer is ", subans)
    elif Menuchoice == 3:
        print ("Division - divide numbers..")
        div1 = int(input("Enter your first number: "))
        div2 = int(input("Enter your second number: "))
        divans = div1 / div2
        print ("The answer is ", divans)
    elif Menuchoice == 4:
        print ("Multiplication - multiply numbers..")
        mul1 = int(input("Enter your first number: "))
        mul2 = int(input("Enter your second number: "))
        mulans = mul1 * mul2
        print ("The answer is ", mulans)
    else:
        print ("You entered an incorrect number. 1-4 are the only options. Try Again")
