import re

with open("harry1.txt")as f:
  a=f.read()
b=re.findall('\S+@\S+',a)
# print(type(b))
data="\n".join(map(str,b)).replace(",","\n")
# print((data))
with open("EmailAddressID.txt","w") as f:
 for i in data:
   f.write(data)







