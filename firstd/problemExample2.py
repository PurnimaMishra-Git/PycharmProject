number=int(input("Enter number of apples: "))
Min_number_start=int(input("Enter Minimum number for distribution: "))
Max_number_stop=int(input("Enter Maximum number for distribution: "))


for i in range(Min_number_start,Max_number_stop+1):
 if number%i==0:
     print(f"{i} is divisor of {number}")
 else:print(f"{i} is not divisor of {number}")

