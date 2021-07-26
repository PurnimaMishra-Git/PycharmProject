import random

a=int(input("Enter number for table: "))
c=[a*i for i in range(1,11)]
i=random.randint(1,10)
c[i]=random.randint(a,a*10)
print(f"Table of {a}:{c}")

mul=[a*i for i in range(1,11)]
# print(f"Table with Correct value:{mul}")



for i in range(0,len(c)):
    for i in range(0,len(mul)):
        if c[i]!=mul[i]:
            print(f"Number {c[i]} is incorrect at Index:{i}")
            exit()
