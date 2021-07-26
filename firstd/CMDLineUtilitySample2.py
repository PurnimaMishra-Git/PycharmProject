import argparse
import sys

def calc(args):
    # list = ["+", "*", "/"]
    # for i in list:
    #     print("operator:", i)
    # args.operator = input("Choose Operator: ")
    # args.number1 = int(input("Enter number1: "))
    # args.number2 = int(input("Enter number2: "))
    if args.operator == 'add':
        if args.number1 == 56 and args.number2 == 6:
            return 77
        else:
         return  args.number1 + args.number2
    elif "Mul" == args.operator:
        if args.number1 == 45 and args.number2 == 3:
            print("45*3=555")
        else:
            print(f"{args.number1}*{args.number2}=", args.number1 * args.number2)
    elif "div" == args.operator:
        if args.number1 == 56 and args.number2 == 3:
            print("56/3=4")
        else:
            print(f"{args.number1}/{args.number2}=", args.number1 / args.number2)
    else:
        print("Invalid Input!!!!")


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('op',type= str,help="This is utility for calculator...Contact Purnima Mishra")
    parser.add_argument('num1',type=int,default=1,help="This is utility forcalculator....kindly contact Purnima mishra")
    parser.add_argument('num2',type=int,default=1,help="This is utility forcalculator....kindly contact Purnima mishra")

    args=parser.parse_args()
    sys.stdout.write(calc(args))

