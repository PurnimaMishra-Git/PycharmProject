def function_fact(n):
  fact=1
  for i in range(1,n+1):
    fact = fact* i
  return fact
number=int(input("Enter number:"))
print(function_fact(number))
