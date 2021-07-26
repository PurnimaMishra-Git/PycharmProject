mylist=[]
for n in range(int(input("Enter your list size: "))):
    user_list=int(input("Enter your element: \n"))
    mylist.append(user_list)
print(f"Your element is {list(mylist)}")

reverse1=mylist[:]
reverse1.reverse()
print(f"This is Reverse 1 using reverse method inbuilt {reverse1}")

reverse2=mylist[:]
# reverse2[::-1]
print(f"This is Reverse 2 using reverse method Slicing{mylist[::-1]} ")

reverse3=mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i],reverse3[len(reverse3)-i-1]=reverse3[len(reverse3)-i-1],reverse3[i]
print(f"This is Reverse 3 using reverse method swapping {reverse3}")