n=int(input("Enter a number: "))
sum=0
len=0

while(n!=0):
    d=n%10
    sum=sum+d
    n=n//10
    len+=1

avg=sum/len
print("Avarage of the number: ", round(avg,3))
