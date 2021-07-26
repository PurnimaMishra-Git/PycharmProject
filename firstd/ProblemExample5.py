# This function will tell you if the number is Palindrom or not.

def is_palindrom(n):
    if (str(n) == str(n)[::-1])== True:
     return "Palindrom"
    else:
        return "Not Palindrom"
# This function will tell you for next Palindrom for given number.

def is_next_palindrom(n):
    # n=n+1
    while True:
        n=n+1
        if (str(n) == str(n)[::-1]) == True:
         return n
         break

# This is main for taking input list from user for number and calling function for Palindrom and Next Palindrom.

if __name__ == '__main__':
    try:
        size=int(input("Enter Size:"))
        mylist=[]
        for number in range(size):
          element=int(input("Enter Element: "))
          mylist.append(element)

        for number in mylist:
          print(f"Number {number} is {is_palindrom(number)}")
          print(f"For Number {number} next palindrom is {is_next_palindrom(number)}")
    except ValueError:
        print(" Kindly enter valid input!!!")



