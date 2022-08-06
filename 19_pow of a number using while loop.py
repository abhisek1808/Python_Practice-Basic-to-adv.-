n=int(input("Enter the base number: "))
e=int(input("Enter the exp. number: "))

result=1

while(e!=0):
    result=result*n
    e-=1

print(result)
