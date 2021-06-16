n=int(input("enter the numbers"))
sum=0

while n>0:
    rem=n%10
    square=rem*rem
    sum+=square
    n=n//10
if sum == 1:
    print("I is a Happy number")
else:
    n=sum
    while sum>1:
        while n>0:
            rem=n%10
            square=rem*rem
            sum+=square
            n=n//10
    print("not a happy number")
        
        
