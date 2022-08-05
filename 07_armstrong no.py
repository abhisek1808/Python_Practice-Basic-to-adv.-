n=int(input("Enter a number: "))
num=n
sum=0
while(n!=0):
    d=n%10
    sum=sum+(pow(d,3))
    n=n//10

if (sum==num):
    print(num,"is a aramstron number.")
else:
    print(num,"not a armstrong")