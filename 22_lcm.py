num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

if num1>num2:
    g=num1
else:
    g=num2

while(True):
    if((g%num1==0) and(g%num2==0)):
        lcm=g
        break
    g+=1
    
print(lcm)



