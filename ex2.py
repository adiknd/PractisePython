num = int(input("Enter a number to check: "))
check = int(input("Enter a number to divide by: "))

if num % check == 0:
    if num % 4 == 0:
        print("The number divides evenly into %s" % (check))
    else:
        print("The number divides evenly into %s" % (check))
else:
    print("The number is NOT divides evenly into %s" % (check))
