def userInput():
    global userIn
    userIn = None
    while userIn is None:
        random = input("Please enter a positive integer: ")
        try:
            userIn = int(random)
        except ValueError:
            print("This is not a valid input.")
    if userIn < 0:         
        userInput() 
    return userIn

def testUser():
    global userTest
    userTest = None
    while userTest is None:
        raw = input("Please enter any number: ")
        try:
            userTest = float(raw)
        except ValueError:
            print("This is not a valid input.")
    return userTest

def programmer():
    integer = userInput()
    binAnswer = ""
    i = 0
    while i < 1:
        modded = integer % 2
        if modded == 1:
            binAnswer = "1" + binAnswer
        else:
            binAnswer = "0" + binAnswer
        integer = integer // 2
        if integer == 1:
            i += 1
            binAnswer = "1" + binAnswer
        elif integer == 0:
            i += 1
    print("Binary equivalent: " + binAnswer)

def scientific():
    operator = str(input("Please choose an operator (+, -, *, /, or **): "))
    if operator == "+":
        op1 = testUser()
        op2 = testUser()
        print(str(op1 + op2))
    elif operator == "-":
        op1 = testUser()
        op2 = testUser()
        print(str(op1 - op2))
    elif operator == "*":
        op1 = testUser()
        op2 = testUser()
        print(str(op1 * op2))
    elif operator == "/":
        op1 = testUser()
        op2 = testUser()
        print(str(op1 / op2))
    elif operator == "**":
        op1 = testUser()
        op2 = testUser()
        print(str(op1 ** op2))
    else:
        print("That was not a valid input.")
        scientific()

def again():
    z = 0
    userAgain = input("Again? y/n: ")
    if userAgain == "n":
        z += 1 
        return z
    elif userAgain == "y":
        z = 0
        return z
    else:
        return again()

x = 0
while x < 1:
    j = 0
    print() 
    mode = input("Please select a mode (p for programmer, s for scientific, q for quit): ")
    while j < 1:
        if mode == "p":
            programmer()
            j = again()
        elif mode == "s":
            scientific()
            j = again()
        elif mode == "q":
            j += 1
            x += 1
        else:
            j += 1
