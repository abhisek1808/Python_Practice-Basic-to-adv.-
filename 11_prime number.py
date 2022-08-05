n=int(input("Enter a number: "))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
        print(i)

if (c!=2):
    print("Not a prime number")
else:
    print("It's a prime number")