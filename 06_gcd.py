from numpy import minimum


num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

if num1>num2:
    m=num2
else:
    m=num1

for i in range(1,m+1):
    if((num1%i==0) and (num2%i==0)):
        gcd=i

print(gcd)