import random



user_input=[]
for name in range(0,4):
    a=input("Enter name: ")
    user_input.append(a)

name=" ".join(user_input).split()
mylist=name[:]
jumble1=random.shuffle(name)
jumble_string=name
# print(list(zip(jumble_string,mylist)))

for name in zip(jumble_string,mylist):
    print('{!s}'.format(name).replace(',',''))





