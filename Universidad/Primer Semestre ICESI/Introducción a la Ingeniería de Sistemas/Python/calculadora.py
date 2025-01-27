
def add():
    addition1 = int(input("Insert the first number: "))
    adittion2 = int(input("Insert the second number: "))
    print ("The result is:", addition1+adittion2)

def subtract():
    minuend = int(input("Insert the minuend: "))
    subtrahend = int(input("Insert the substrahend: "))
    print ("The difference is: ", minuend-subtrahend)

def multiply(): 
    multiplying = int(input("Insert the multiplying: "))
    multiplier = int(input("Insert the multiplyer: "))
    print ("The result of the multiplication is: ", multiplying*multiplier)

def divide():
    try:
        dividend = int(input("Insert the dividend: "))
        divisor = int(input("Insert the divisor: "))
        print ("The result of the division is: ", dividend/divisor)
    except ZeroDivisionError: 
        print ("ERROR")
def Calculator():
    end = False
    while not(end):
        opc = int(input("Option:"))
        if (opc==1):
            add()
        elif(opc==2):
            subtract()
        elif(opc==3):
            multiply()
        elif(opc==4):
            divide()
        elif(opc==5):
            end = 1

print("""**********
Calculator
**********
Menu
1) ADD
2) SUBTRACT
3) MULTIPLY
4) DIVIDE
5) END""")
Calculator ()