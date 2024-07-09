import random
import time
import calcfuncs

cf = calcfuncs.Calc()

print("Enter choice: \
      1: Add \
      2: Subtract \
      3: Divide \
      4: Multiply \
      5: Sin(x) approximated")
choice = int(input("Enter choice: "))

if choice != None :
    if choice == 1 :
        x = int(input("Enter num1: "))
        y = int(input("Enter num2: "))
        print(cf.add(x, y))
    elif choice == 2 :
        x = int(input("Enter num1: "))
        y = int(input("Enter num2: "))
        print(cf.subtract(x, y))
    elif choice == 3:
        x = int(input("Enter num1: "))
        y = int(input("Enter num2: "))
        print(cf.divide(x, y))
    elif choice == 4:
        x = int(input("Enter num1: "))
        y = int(input("Enter num2: "))
        print(cf.multiply(x, y))
    elif choice == 5:
        x = int(input("Enter num1: "))
        print(cf.sin(x))
    else:
        raise NotImplementedError("That function doesn't exist, poopyhead");
else:
    raise Exception("Can't enter nothing brozo")