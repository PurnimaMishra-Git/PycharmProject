def take(k):
    if (k==1):
        c=int(input("Enter 1 for food and 2 for Excersize:"))
        if (c==1):
            with open("harry1.txt","a") as f:
                a = input(f)
                f.write(a)
        elif (c==2):
         with open("harry2.txt", "a") as f:
            a = input(f)
            f.write(a)

    elif (k==2):
        c=int(input("Enter 1 for food and 2 for Excersize:"))
        if (c==1):
            with open("rohan1.txt","a") as f:
                a = input(f)
                f.write(a)
        elif (c==2):
         with open("rohan2.txt", "a") as f:
            a = input(f)
            f.write(a)

    elif (k==3):
        c=int(input("Enter 1 for food and 2 for Excersize:"))
        if (c==1):
            with open("hamad1.txt","a") as f:
                a = input(f)
                f.write(a)
        elif (c==2):
         with open("hamad2.txt", "a") as f:
            a = input(f)
            f.write(a)
    else:print("invalid input")

def ret(k):
    if (k == 1):
        c = int(input("Enter 1 for food and 2 for Excersize:"))
        if (c == 1):
            with open("harry1.txt") as f:
                a=f.read()
                print(a)
        elif (c == 2):
            with open("harry2.txt") as f:
                a=f.read()
                print(a)
    else:
        print("invalid input")


number=(int(input("enter 1 for harry 2 for rohan 3 for hamad:")))
take(number)
# number2=(str(input("ret:")))
# ret(1)

