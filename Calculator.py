print("This is a mathematical calculator where you have to enter 0 for Addition")
print("                                                          1 for Subtraction")
print("                                                          2 for Multiplication")
print("                                                          3 for Division")
x = float(input("Enter the first number \n"))
y = float(input("Enter the second number \n"))
P = int(input("Enter the digit corresponding to arithmetic operation \n"))
def add():
    print ("The result of the Addition is",(x+y))
def sub():
    print ("The result of the Subtraction is",(x-y))
def mul():
    print ("The result of the Multiplication is",(x*y))
def div():
    if y!=0:
        print ("The result of the Division is",(x/y))
    elif y==0:
        print ("Division not possible")
def xyz(l):
    switcher={
    0:add,
    1:sub,
    2:mul,
    3:div,
    }
    return switcher.get(l,input("Option not available \n"))
output=(xyz(P))
output()
input("Press enter to exit ;)")




