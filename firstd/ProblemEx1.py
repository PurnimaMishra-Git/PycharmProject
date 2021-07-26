# Problem Practical 1

current_yr = 2021
# while True:
print("1.Enter your Age: \n2.Enter Birth Year: ")
user_choice = int(input("Please Enter Your Choice:"))
# User_input_Age = int(input("1.Enter your Age: \n2.Enter Birth Year: "))


if user_choice==1:
    User_input_Age = int(input("Enter your Age: "))
    if User_input_Age>100 and User_input_Age<150:
      print("You seems to be oldest person alive!!")
    if User_input_Age in range(0,101):
      b=100-User_input_Age
      print(f"You will turn 100 year old in {b} years")

elif user_choice==2:
    current_yr=2021
    User_input_yr = int(input("Enter Birth Year: "))
    Current_age=current_yr-User_input_yr
    if len(str(User_input_yr)) not in range(0,5) or len(str(User_input_yr)) in range(0,4):
        print("Invalid Year")
    if User_input_yr==current_yr:
        print(f"Congratulations!!!\nThis is your born year.")
    if Current_age>100 and Current_age<150:
        print("You seems to be oldest person alive!!")
    if Current_age in range(0,101):
        c=100-Current_age
        print(f"you will turn 100 Year old in {c} years")
    if User_input_yr>current_yr:
        print("You are not yet born!!")


else:print("Invalid Input!!!")
# continue




