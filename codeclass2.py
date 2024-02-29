print("Welcome to the python calculator!!")
name_=str(input("Please Eter your name???"))
opt__ = int(input("""Enter the option Below??
                # for addition--> (1) 
                # for subtraction -->  (2)
                # for division -->  (3)
                # for multiplication -->  (4)
                 ------->>>"""))
if opt__==1:
    num1=float(input("please Enter the first  number?"))
    num2=float(input("PLease Enter the second number?"))
    x=num1+num2
    print(f"Your Answer is: {x} ")
elif opt__==2:
    num1=float(input("please Enter the first  number?"))
    num2=float(input("PLease Enter the second number?"))
    x=num1-num2
    print(f"Your Answer is: {x} ")
elif opt__==3:
    num1=float(input("please Enter the first  number?"))
    num2=float(input("PLease Enter the second number?"))
    x=num1/num2
    print(f"Your Answer is: {x} ")
elif opt__==4:
    num1=float(input("please Enter the first  number?"))
    num2=float(input("PLease Enter the second number?"))
    x=num1*num2
    print(f"Your Answer is: {x} ")
else :
    print("""UNknown option entered!!! 
           please try again !!""")


