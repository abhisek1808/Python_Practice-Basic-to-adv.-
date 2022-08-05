n=int(input("Enter Your number :"))
fact=1

if (n < 0):
    fact=0
else:
    for i in range (1,n+1):
        fact=fact*i
print("The factorial of",n, "is :", fact )




 

