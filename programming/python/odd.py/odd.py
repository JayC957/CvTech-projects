#Jay William Camp Jr
#5/1/25


#gets input from user as a float
number = float(input("Enter a number: "))
#checks odd or evem
if number.is_integer():
    if int(number) % 2 == 0:
        print("Even")
    else:
        print("Odd")
#I know you would check do
else:
    print("Not a whole number")