# Faulty Calculator Programme

list=["+","*","/"]
for i in list:
    print("operator:",i)
a=input("Choose Operator: ")
number1=int(input("Enter number1: "))
number2=int(input("Enter number2: "))
if list[0]== a:
    if number1== 56 and number2== 6:
        print("56+6=77")
        print(type(a))
        print(type(list[0]))
    else:print(f"{number1}+{number2}=", number1+number2)
elif list[1] == a:
    if number1 == 45 and number2 == 3:
        print("45*3=555")
    else:
        print(f"{number1}*{number2}=", number1 * number2)
elif list[2] == a:
    if number1 == 56 and number2 == 3:
        print("56/3=4")
    else:
        print(f"{number1}/{number2}=", number1 / number2)
else:
    print("Invalid Input!!!!")


