n=int(input("Enter a number: "))
sum=0
num=n
fact=1

while(n!=0):
    d=n%10
    for i in range(1,d+1):
        fact=fact*i
    sum=sum+fact
    fact=1
    n=n//10

if(sum==num):
    print(num,"It's a special number")
else:
    print(num,"not a special number")
